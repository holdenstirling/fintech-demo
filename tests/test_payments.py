"""
Payment API tests — FTC-4421 idempotency fix branch.
"""
import app.database as db_module


def test_create_payment_succeeds(client):
    res = client.post("/api/payments", json={
        "amount": 2000, "currency": "usd", "customer_id": "cust_test1"
    })
    assert res.status_code == 201
    data = res.json()
    assert data["amount"] == 2000
    assert data["status"] == "succeeded"
    assert "id" in data


def test_list_payments(client):
    client.post("/api/payments", json={"amount": 500, "currency": "usd", "customer_id": "cust_list"})
    res = client.get("/api/payments")
    assert res.status_code == 200
    assert len(res.json()) >= 1


def test_get_payment_by_id(client):
    create_res = client.post("/api/payments", json={
        "amount": 5000, "currency": "usd", "customer_id": "cust_get"
    })
    pid = create_res.json()["id"]
    res = client.get(f"/api/payments/{pid}")
    assert res.status_code == 200
    assert res.json()["id"] == pid


def test_get_payment_not_found(client):
    res = client.get("/api/payments/does-not-exist")
    assert res.status_code == 404


def test_invalid_amount_rejected(client):
    res = client.post("/api/payments", json={
        "amount": -100, "currency": "usd", "customer_id": "cust_bad"
    })
    assert res.status_code == 422


def test_idempotency_key_prevents_duplicate_charge(client):
    """First request with a key creates a charge (201). Duplicate returns same payment (200)."""
    payload = {"amount": 9900, "currency": "usd", "customer_id": "cust_idem", "description": "Invoice #8821"}
    key = "test-idem-key-abc123"

    res = client.post("/api/payments", json=payload, headers={"Idempotency-Key": key})
    assert res.status_code == 201
    first_id = res.json()["id"]

    res2 = client.post("/api/payments", json=payload, headers={"Idempotency-Key": key})
    assert res2.status_code == 200
    assert res2.json()["id"] == first_id, "Duplicate request must return the original payment ID"


def test_different_keys_create_separate_charges(client):
    """Two requests with different keys each create a new charge."""
    payload = {"amount": 5000, "currency": "usd", "customer_id": "cust_two"}
    r1 = client.post("/api/payments", json=payload, headers={"Idempotency-Key": "key-one"})
    r2 = client.post("/api/payments", json=payload, headers={"Idempotency-Key": "key-two"})
    assert r1.json()["id"] != r2.json()["id"]


def test_no_key_still_works(client):
    """Requests without idempotency key continue to work (backwards compatible)."""
    res = client.post("/api/payments", json={
        "amount": 1000, "currency": "usd", "customer_id": "cust_nokey"
    })
    assert res.status_code == 201


def test_expired_idempotency_key_creates_new_charge(client):
    """
    An expired idempotency key (> 24 hours old) must NOT return the cached result.
    A new charge should be created instead.

    Acceptance criterion from ISSUE.md: keys expire after 24 hours.
    """
    import json
    from datetime import datetime, timedelta

    key = "test-expired-key-xyz"
    # Seed an idempotency key that's 25 hours old (expired)
    expired_ts = (datetime.utcnow() - timedelta(hours=25)).strftime("%Y-%m-%d %H:%M:%S")
    stale_response = json.dumps({"id": "old-payment-id", "amount": 9900, "currency": "usd",
                                  "customer_id": "cust_exp", "status": "succeeded",
                                  "description": None, "created_at": expired_ts})
    with db_module.get_connection() as conn:
        conn.execute(
            "INSERT INTO idempotency_keys (idempotency_key, payment_response, created_at) VALUES (?, ?, ?)",
            (key, stale_response, expired_ts),
        )

    # Request with expired key should process a NEW charge, not return the stale one
    res = client.post("/api/payments", json={
        "amount": 9900, "currency": "usd", "customer_id": "cust_exp"
    }, headers={"Idempotency-Key": key})

    assert res.status_code == 201
    assert res.json()["id"] != "old-payment-id", "Expired key must not return the stale cached payment"
