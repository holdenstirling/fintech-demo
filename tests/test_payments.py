"""
Payment API tests.

Note: test_duplicate_charge_without_idempotency_key intentionally demonstrates
the open bug FTC-4421. It is expected to PASS (proving the bug exists) until
idempotency key support is implemented.
"""


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


def test_duplicate_charge_without_idempotency_key(client):
    """
    Demonstrates bug FTC-4421: submitting the same payment twice produces two
    separate charges. This test PASSES today (proving the bug exists).

    Once idempotency key support is implemented, this test should be updated:
    - Requests with the same Idempotency-Key should return the SAME payment ID
    - Only one charge should exist in the database
    """
    payload = {"amount": 9900, "currency": "usd", "customer_id": "cust_dupe", "description": "Invoice #8821"}

    res1 = client.post("/api/payments", json=payload)
    res2 = client.post("/api/payments", json=payload)

    assert res1.status_code == 201
    assert res2.status_code == 201

    # Two different IDs = two separate charges. This is the bug.
    assert res1.json()["id"] != res2.json()["id"], (
        "Expected two distinct charge IDs (bug FTC-4421 is present)"
    )
