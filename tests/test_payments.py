"""
Payment API tests.
"""
import uuid
from datetime import datetime, timedelta
import app.database as db_module
from app.config import INTERNAL_API_KEY

# Shared auth header used by all endpoints that require Bearer authentication.
AUTH = {"Authorization": f"Bearer {INTERNAL_API_KEY}"}


def test_create_payment_succeeds(client):
    res = client.post("/api/payments", json={
        "amount": 2000, "currency": "usd", "customer_id": "cust_test1"
    }, headers=AUTH)
    assert res.status_code == 201
    data = res.json()
    assert data["amount"] == 2000
    assert data["status"] == "succeeded"
    assert "id" in data


def test_create_payment_requires_auth(client):
    res = client.post("/api/payments", json={
        "amount": 2000, "currency": "usd", "customer_id": "cust_test1"
    })
    assert res.status_code == 401


def test_list_payments(client):
    client.post("/api/payments", json={"amount": 500, "currency": "usd", "customer_id": "cust_list"}, headers=AUTH)
    res = client.get("/api/payments", headers=AUTH)
    assert res.status_code == 200
    assert len(res.json()) >= 1


def test_list_payments_requires_auth(client):
    res = client.get("/api/payments")
    assert res.status_code == 401


def test_get_payment_by_id(client):
    create_res = client.post("/api/payments", json={
        "amount": 5000, "currency": "usd", "customer_id": "cust_get"
    }, headers=AUTH)
    pid = create_res.json()["id"]
    res = client.get(f"/api/payments/{pid}", headers=AUTH)
    assert res.status_code == 200
    assert res.json()["id"] == pid


def test_get_payment_not_found(client):
    res = client.get("/api/payments/does-not-exist", headers=AUTH)
    assert res.status_code == 404


def test_get_payment_requires_auth(client):
    res = client.get("/api/payments/some-id")
    assert res.status_code == 401


def test_invalid_amount_rejected(client):
    res = client.post("/api/payments", json={
        "amount": -100, "currency": "usd", "customer_id": "cust_bad"
    }, headers=AUTH)
    assert res.status_code == 422


def test_invalid_bearer_token_rejected(client):
    res = client.get("/api/payments", headers={"Authorization": "Bearer wrong_token"})
    assert res.status_code == 401


# ── Idempotency tests (FTC-4421) ──────────────────────────────────────────────

def test_idempotency_new_key_returns_201(client):
    """A request with a fresh idempotency key creates a new charge and returns 201."""
    key = str(uuid.uuid4())
    res = client.post(
        "/api/payments",
        json={"amount": 9900, "currency": "usd", "customer_id": "cust_idem"},
        headers={"Idempotency-Key": key, **AUTH},
    )
    assert res.status_code == 201
    assert "id" in res.json()


def test_idempotency_duplicate_key_returns_200_same_id(client):
    """A retried request with the same idempotency key returns 200 with the original payment ID."""
    key = str(uuid.uuid4())
    payload = {"amount": 9900, "currency": "usd", "customer_id": "cust_dupe", "description": "Invoice #8821"}

    res1 = client.post("/api/payments", json=payload, headers={"Idempotency-Key": key, **AUTH})
    res2 = client.post("/api/payments", json=payload, headers={"Idempotency-Key": key, **AUTH})

    assert res1.status_code == 201
    assert res2.status_code == 200
    assert res1.json()["id"] == res2.json()["id"], "Duplicate key must return the original payment ID"


def test_idempotency_expired_key_creates_new_charge(client):
    """An idempotency key older than 24 hours is treated as new — a fresh charge is created."""
    key = str(uuid.uuid4())
    payload = {"amount": 1500, "currency": "usd", "customer_id": "cust_expired"}

    # Create the first payment and then backdating its idempotency key to 25 hours ago
    res1 = client.post("/api/payments", json=payload, headers={"Idempotency-Key": key, **AUTH})
    assert res1.status_code == 201

    expired_ts = (datetime.utcnow() - timedelta(hours=25)).strftime("%Y-%m-%d %H:%M:%S")
    with db_module.get_connection() as conn:
        conn.execute(
            "UPDATE idempotency_keys SET created_at = ? WHERE key = ?",
            (expired_ts, key),
        )

    # Retry with the same key — key is expired so a new charge is issued
    res2 = client.post("/api/payments", json=payload, headers={"Idempotency-Key": key, **AUTH})
    assert res2.status_code == 201
    assert res1.json()["id"] != res2.json()["id"], "Expired key must result in a new charge"


def test_no_idempotency_key_still_creates_payment(client):
    """Requests without an idempotency key continue to work; each creates a new charge."""
    payload = {"amount": 9900, "currency": "usd", "customer_id": "cust_nokey"}
    res1 = client.post("/api/payments", json=payload, headers=AUTH)
    res2 = client.post("/api/payments", json=payload, headers=AUTH)
    assert res1.status_code == 201
    assert res2.status_code == 201
    assert res1.json()["id"] != res2.json()["id"]
