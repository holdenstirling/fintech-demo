from contextlib import asynccontextmanager
from typing import List
from fastapi import FastAPI, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.models import PaymentRequest, PaymentResponse
from app import payments
from app.database import init_db, get_connection


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="FinTechCo Payments API", version="2.1.4", lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")


# ── Frontend ──────────────────────────────────────────────────────────────────

@app.get("/", include_in_schema=False)
async def serve_dashboard():
    return FileResponse("static/index.html")


# ── Payments API ──────────────────────────────────────────────────────────────

@app.post("/api/payments", response_model=PaymentResponse, status_code=201)
async def create_payment(payment: PaymentRequest):
    """
    Process a payment charge.

    WARNING: No idempotency key support. Retried requests create duplicate charges.
    See ISSUE.md — ticket FTC-4421.
    """
    return payments.create_payment(payment)


@app.get("/api/payments", response_model=List[PaymentResponse])
async def list_payments(limit: int = Query(50, le=200)):
    return payments.list_payments(limit)


@app.get("/api/payments/search", response_model=List[PaymentResponse])
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

@app.get("/api/admin/payments", response_model=List[PaymentResponse])
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
