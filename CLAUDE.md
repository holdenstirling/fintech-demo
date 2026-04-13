# FinTechCo Payments Service

This is a PCI-DSS regulated payment processing service. All contributors must follow these guidelines.

## Security Requirements

- **Never hardcode secrets** — API keys, tokens, and passwords must come from environment variables
- **Parameterized queries only** — string interpolation in SQL is a critical vulnerability (SQL injection)
- **Authentication required** — every endpoint that reads or writes payment data must verify a Bearer token
- **Rate limiting** — all public-facing endpoints must have rate limits configured
- **No PII in logs** — never log card numbers, CVV, raw PANs, or full customer records

## Architecture Rules

- All payment charges must go through `create_payment()` in `app/payments.py`
- External processor calls are isolated in `app/processor.py` — do not call the processor directly from routes
- Database access goes through `get_connection()` in `app/database.py`
- Configuration values come from `app/config.py` — no inline config in route files

## Idempotency (required for all state-mutating endpoints)

- All `POST` endpoints that create resources must support an `Idempotency-Key` header
- Keys are UUID v4 strings, expire after 24 hours, stored in `idempotency_keys` table
- Duplicate requests return HTTP `200` with the original response body
- First-time requests return HTTP `201`

## Coding Conventions

- Python 3.9+ compatible type hints (`Optional[X]`, `List[X]` from `typing`)
- All route return types must be Pydantic models
- Use `snake_case` for functions and variables, `PascalCase` for classes
- Keep route handlers thin — business logic lives in service modules, not `main.py`

## Testing

- Every new endpoint needs tests in `tests/test_payments.py`
- Use the `isolated_db` fixture — never touch the real database in tests
- New idempotency features must include tests for: new key, duplicate key, expired key
- Run `pytest` before committing — all tests must be green

## Before You Ship

- [ ] `pytest` passes
- [ ] No hardcoded secrets (`grep -r "sk_live\|api_key\s*=" app/`)
- [ ] No raw SQL string interpolation
- [ ] New endpoints have authentication
- [ ] ISSUE.md updated if a ticket is resolved
