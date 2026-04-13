from typing import Optional
from fastapi import FastAPI, HTTPException, Query, Header
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.models import PaymentRequest, PaymentResponse
from app import payments
from app.database import init_db, get_connection, get_idempotency_result, store_idempotency_result

app = FastAPI(title="FinTechCo Payments API", version="2.1.4")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.on_event("startup")
async def startup():
    init_db()


# ── Frontend ──────────────────────────────────────────────────────────────────

@app.get("/", include_in_schema=False)
async def serve_dashboard():
    return FileResponse("static/index.html")


# ── Payments API ──────────────────────────────────────────────────────────────

@app.post("/api/payments", status_code=201)
async def create_payment(
    payment: PaymentRequest,
    idempotency_key: Optional[str] = Header(None, alias="Idempotency-Key"),
):
    """
    Process a payment charge.

    Supports idempotency keys via the `Idempotency-Key` header.
    Duplicate requests with the same key return the original response (HTTP 200).
    First-time requests return HTTP 201.
    """
    if idempotency_key:
        cached = get_idempotency_result(idempotency_key)
        if cached:
            return JSONResponse(content=cached, status_code=200)

    result = payments.create_payment(payment)

    if idempotency_key:
        store_idempotency_result(idempotency_key, result.dict())

    return result


@app.get("/api/payments", response_model=list[PaymentResponse])
async def list_payments(limit: int = Query(50, le=200)):
    return payments.list_payments(limit)


@app.get("/api/payments/search", response_model=list[PaymentResponse])
async def search_payments(customer_id: str):
    """Search payments by customer ID."""
    with get_connection() as conn:
        # BUG: raw string interpolation — vulnerable to SQL injection
        rows = conn.execute(
            f"SELECT * FROM payments WHERE customer_id = '{customer_id}' ORDER BY created_at DESC"
        ).fetchall()
    from app.payments import _row_to_response
    return [_row_to_response(r) for r in rows]


@app.get("/api/payments/{payment_id}", response_model=PaymentResponse)
async def get_payment(payment_id: str):
    payment = payments.get_payment(payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment


# ── Admin ─────────────────────────────────────────────────────────────────────

@app.get("/api/admin/payments", response_model=list[PaymentResponse])
async def admin_list_all_payments():
    """
    Returns full payment history for all customers.
    Internal use only.
    """
    # SECURITY: No authentication check — any caller can access all payment records
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM payments ORDER BY created_at DESC"
        ).fetchall()
    from app.payments import _row_to_response
    return [_row_to_response(r) for r in rows]


# ── Health ────────────────────────────────────────────────────────────────────

@app.get("/health")
async def health():
    return {"status": "ok", "version": "2.1.4"}
