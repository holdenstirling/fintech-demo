# FinTechCo Payments Service

PCI-DSS regulated payment processing service. All contributors must follow these guidelines.
Violations are not style issues — they are audit findings.

## Security Requirements

### Secrets
- **Never hardcode secrets** — API keys, tokens, and passwords must come from environment variables
- `os.environ.get("KEY")` with no fallback is correct; `os.environ.get("KEY", "sk_live_...")` is not — a hardcoded fallback is a hardcoded secret
- The service must refuse to start if required secrets are absent, not silently use a default
- Check before committing: `grep -r "sk_live\|api_key\s*=\|whsec_\|ftco_internal" app/`

### Authentication
- Every endpoint that reads or writes payment data must call `_require_bearer()` (`app/main.py`)
- `_require_bearer()` uses `hmac.compare_digest` — **do not replace this with `==` or `!=`**. String equality short-circuits and leaks timing information that enables token enumeration
- The pattern for a protected route:
  ```python
  async def my_endpoint(authorization: Optional[str] = Header(None)):
      _require_bearer(authorization)
      ...
  ```

### SQL
- **Parameterized queries only** — never use f-strings or `%` formatting in SQL
- Correct: `conn.execute("SELECT * FROM payments WHERE id = ?", (payment_id,))`
- Wrong: `conn.execute(f"SELECT * FROM payments WHERE id = '{payment_id}'")`

### Logging and PII
- Never log card numbers, CVV, raw PANs, or full customer records
- `customer_id` is safe to log; `amount` is safe to log; raw request bodies are not

### Rate limiting
- All public-facing endpoints must have rate limits configured before going to production

## Architecture Rules

- All payment charges go through `create_payment()` in `app/payments.py` — never call `processor.charge()` from a route
- External processor calls are isolated in `app/processor.py`
- Database access goes through `get_connection()` in `app/database.py`
- Configuration values come from `app/config.py` — no inline config in route files
- **No SQL queries in route handlers** — all database logic belongs in service modules (`payments.py`). Route handlers call service functions and return their results
- Seed data (`_seed_demo_data`) must not run when `ENVIRONMENT=production`

## Idempotency (required for all state-mutating endpoints)

All `POST` endpoints that create resources must support idempotency. This requirement exists because
network retries are indistinguishable from duplicate requests — without idempotency, retries cause
double-charges (see incident FTC-4421).

### Application-layer rules
- Accept an optional `Idempotency-Key: <uuid-v4>` header on every state-mutating endpoint
- Before processing: check `idempotency_keys` table for the key
- If found and not expired: return the original response body with HTTP `200` — do not charge again
- If not found or expired: process normally, store `(key, payment_id)`, return HTTP `201`
- Keys expire after 24 hours (`IDEMPOTENCY_KEY_TTL_HOURS = 24` in `payments.py`)
- Keys are stored in the `idempotency_keys` table (`key`, `payment_id`, `created_at`)
- Requests with no `Idempotency-Key` must still work — the header is optional for backwards compatibility

### Processor-layer rule
- The idempotency key sent to the external processor (`app/processor.py`) must be derived from a
  **stable value** — use the payment ID or the application-level idempotency key, not `uuid.uuid4()`
- A fresh random UUID on every call means processor-level retries are not safe and can cause
  double-charges even when our application layer is correct

### Error handling
- Wrap `processor.charge()` in a try/except that distinguishes two failure modes:
  - **Charge definitively rejected** (4xx from processor): safe to return an error to the caller
  - **Charge outcome unknown** (timeout, 5xx, connection error): do not return a success or a clean failure — this state requires reconciliation. Log with full context and alert

## Coding Conventions

- Python 3.9+ compatible type hints (`Optional[X]`, `List[X]` from `typing`)
- All route return types must be Pydantic models
- Use `snake_case` for functions and variables, `PascalCase` for classes
- Keep route handlers thin — business logic lives in service modules, not `main.py`

## Testing

- Every new endpoint needs tests in `tests/test_payments.py`
- Use the `isolated_db` fixture (autouse in `conftest.py`) — never touch the real database in tests
- Import `INTERNAL_API_KEY` from `app.config` and construct `AUTH = {"Authorization": f"Bearer {INTERNAL_API_KEY}"}` once at the top of the test file; pass it to every request that hits a protected endpoint
- **Every protected endpoint needs a 401 test** — confirm the endpoint rejects requests with no token and with a wrong token, not just that it accepts valid ones
- **Every idempotency-capable endpoint needs three tests**: new key (expect 201), duplicate key (expect 200 + same ID), expired key (expect 201 + new ID)
- Run `pytest` before committing — all tests must be green

## Before You Ship

- [ ] `pytest` passes with no failures or warnings that hide real errors
- [ ] No hardcoded secrets or live-key fallbacks (`grep -r "sk_live\|whsec_\|ftco_internal" app/`)
- [ ] No raw SQL string interpolation (`grep -rn 'execute(f\|execute(".*%' app/`)
- [ ] Every new or modified endpoint calls `_require_bearer()` and has a corresponding 401 test
- [ ] Every new state-mutating endpoint has idempotency tests: new key, duplicate key, expired key
- [ ] Processor calls have error handling that distinguishes rejected vs unknown-state outcomes
- [ ] `ISSUE.md` updated if a ticket is resolved
