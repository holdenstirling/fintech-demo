import hmac
import random
import string
from contextlib import asynccontextmanager
from datetime import datetime
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Query, Header, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.models import PaymentRequest, PaymentResponse
from app import payments
from app.database import init_db, get_connection
from app.config import INTERNAL_API_KEY

# ── Demo incident state (resets on server restart — that's intentional) ────────
_server_start: str = datetime.utcnow().isoformat()
_p1_active: bool = False
_p1_customer: str = ""
_pr_info: Optional[dict] = None


def _require_bearer(authorization: Optional[str]) -> None:
    """Raise 401 if the Authorization header is absent or the token is invalid.

    Uses hmac.compare_digest to prevent timing-based token enumeration.
    """
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization header")
    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer" or not hmac.compare_digest(token, INTERNAL_API_KEY):
        raise HTTPException(status_code=401, detail="Invalid or missing Bearer token")


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
async def create_payment(
    payment: PaymentRequest,
    response: Response,
    idempotency_key: Optional[str] = Header(None, alias="Idempotency-Key"),
    authorization: Optional[str] = Header(None),
):
    """
    Process a payment charge.

    Supply an Idempotency-Key header (UUID v4) to safely retry without creating
    duplicate charges. Duplicate requests return HTTP 200 with the original
    response body. First-time requests return HTTP 201.
    """
    _require_bearer(authorization)
    result, is_duplicate = payments.create_payment(payment, idempotency_key)
    if is_duplicate:
        response.status_code = 200
    return result


@app.get("/api/payments", response_model=List[PaymentResponse])
async def list_payments(
    limit: int = Query(50, le=200),
    authorization: Optional[str] = Header(None),
):
    _require_bearer(authorization)
    return payments.list_payments(limit)


@app.get("/api/payments/search", response_model=List[PaymentResponse])
async def search_payments(
    customer_id: str,
    authorization: Optional[str] = Header(None),
):
    """Search payments by customer ID."""
    _require_bearer(authorization)
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM payments WHERE customer_id = ? ORDER BY created_at DESC",
            (customer_id,),
        ).fetchall()
    from app.payments import _row_to_response
    return [_row_to_response(r) for r in rows]


@app.get("/api/payments/{payment_id}", response_model=PaymentResponse)
async def get_payment(
    payment_id: str,
    authorization: Optional[str] = Header(None),
):
    _require_bearer(authorization)
    payment = payments.get_payment(payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment


# ── Admin ─────────────────────────────────────────────────────────────────────

@app.get("/api/admin/payments", response_model=List[PaymentResponse])
async def admin_list_all_payments(authorization: Optional[str] = Header(None)):
    """
    Returns full payment history for all customers.
    Internal use only. Requires a valid Bearer token matching INTERNAL_API_KEY.
    """
    _require_bearer(authorization)
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM payments ORDER BY created_at DESC"
        ).fetchall()
    from app.payments import _row_to_response
    return [_row_to_response(r) for r in rows]


# ── Health & demo status ──────────────────────────────────────────────────────

@app.get("/health")
async def health():
    return {"status": "ok", "version": "2.1.4"}


@app.get("/api/status")
async def get_status():
    """Dashboard polls this to drive the P1 banner and success rate card.
    No auth required — the dashboard needs this before the user logs in.
    Resets automatically when the server restarts (uvicorn --reload after a fix).
    """
    return {
        "p1_active": _p1_active,
        "success_rate": 94.1 if _p1_active else 99.2,
        "incident": "FTC-4421" if _p1_active else None,
        "customer": _p1_customer,
        "server_start": _server_start,
        "pr": _pr_info,
    }


@app.post("/api/simulate-p1")
async def simulate_p1(authorization: Optional[str] = Header(None)):
    """Trigger the FTC-4421 duplicate-charge incident for the demo.
    Creates two identical charges with no idempotency key, sets the P1 flag.
    Flag resets on server restart — which happens automatically when the fix lands.
    """
    _require_bearer(authorization)
    global _p1_active, _p1_customer

    _p1_active = True
    customer = "cust_" + "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    _p1_customer = customer

    payload = PaymentRequest(
        amount=9900,
        currency="usd",
        customer_id=customer,
        description="Invoice #8821",
    )
    result1, _ = payments.create_payment(payload, None)
    result2, _ = payments.create_payment(payload, None)

    return {
        "customer": customer,
        "charge_1": result1.id,
        "charge_2": result2.id,
        "message": f"P1 active: {customer} charged $198.00 instead of $99.00",
    }


@app.post("/api/notify-pr")
async def notify_pr(
    body: dict,
    authorization: Optional[str] = Header(None),
):
    """Notify the dashboard that a PR has been opened for review.
    Called after `gh pr create` to drive the approval banner in the UI.
    Resets on server restart (same as P1 state).
    """
    _require_bearer(authorization)
    global _pr_info
    _pr_info = {
        "number": body.get("number"),
        "title": body.get("title"),
        "url": body.get("url"),
        "status": body.get("status", "open"),
    }
    return _pr_info
