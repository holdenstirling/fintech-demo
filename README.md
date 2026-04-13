# FinTechCo Payments API

Internal payments processing service — digital payments division.

## Setup

```bash
cd fintech-demo
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

Open http://localhost:8000

## Test

```bash
pytest
```

## API

| Method | Path | Description |
|--------|------|-------------|
| POST | /api/payments | Create a payment |
| GET | /api/payments | List recent payments |
| GET | /api/payments/{id} | Get payment by ID |
| GET | /api/payments/search?customer_id= | Search by customer |
| GET | /api/admin/payments | All payments (admin) |

## Open Issues

- **FTC-4421** (P1): Duplicate charges on network retries — see `ISSUE.md`
