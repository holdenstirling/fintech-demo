# FTC-4421 — Duplicate charges on network retries

**Priority:** P1 — Active customer impact  
**Reporter:** Payments Infrastructure  
**Assignee:** Unassigned  

---

## Problem

Customers are being double-charged when their client retries a payment request after a network timeout.

**Root cause:** `POST /api/payments` has no idempotency key support. If a client sends the same request twice — intentionally or due to a timeout — two separate charges are created and two separate records are inserted into the database.

**Confirmed incidents:**
- `cust_A1B2` — charged $99.00 twice on 2026-04-08 (support ticket #48821)
- `cust_E5F6` — charged $199.00 twice on 2026-04-09 (support ticket #48834)

---

## Proposed Solution

Add support for an `Idempotency-Key` request header on `POST /api/payments`.

**Rules:**
1. If a request includes an `Idempotency-Key`, store the key + result after processing
2. If a subsequent request arrives with the **same key**, return the stored result — do not create a new charge
3. Keys should expire after **24 hours**
4. If no `Idempotency-Key` is provided, process normally (backwards compatible)

**Example — first request:**
```
POST /api/payments
Idempotency-Key: a8d3f2c1-9b4e-4f6a-b3c2-1a2b3c4d5e6f
Content-Type: application/json

{ "amount": 9900, "currency": "usd", "customer_id": "cust_A1B2" }
```
→ `201 Created` — charge processed, key stored

**Example — duplicate request (same key):**
```
POST /api/payments
Idempotency-Key: a8d3f2c1-9b4e-4f6a-b3c2-1a2b3c4d5e6f
```
→ `200 OK` — original response returned, **no new charge**

---

## Acceptance Criteria

- [ ] `POST /api/payments` accepts optional `Idempotency-Key` header
- [ ] Duplicate requests with same key return original response (HTTP 200)
- [ ] New `idempotency_keys` table added to database schema
- [ ] Keys expire after 24 hours
- [ ] All existing tests continue to pass
- [ ] New tests cover: new key, duplicate key, expired key behaviour
- [ ] `test_duplicate_charge_without_idempotency_key` updated to assert same ID returned on duplicate
