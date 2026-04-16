"""
Core payment processing logic.
"""
import logging
import uuid
from datetime import datetime, timedelta
from typing import List, Optional, Tuple
from app.database import get_connection
from app.models import PaymentRequest, PaymentResponse
from app import processor

logger = logging.getLogger(__name__)

IDEMPOTENCY_KEY_TTL_HOURS = 24


def create_payment(
    payment: PaymentRequest,
    idempotency_key: Optional[str] = None,
) -> Tuple[PaymentResponse, bool]:
    """
    Process a payment charge.

    Returns a (PaymentResponse, is_duplicate) tuple. is_duplicate is True when
    an idempotency key matches a non-expired prior request; the original response
    is returned and no new charge is issued. is_duplicate is False for new requests.
    """
    if idempotency_key:
        existing = _lookup_idempotency_key(idempotency_key)
        if existing:
            return existing, True

    payment_id = str(uuid.uuid4())
    stable_key = idempotency_key or payment_id

    try:
        proc_result = processor.charge(
            amount=payment.amount,
            currency=payment.currency.value,
            customer_id=payment.customer_id,
            idempotency_key=stable_key,
        )
    except processor.ChargeRejectedError:
        raise
    except processor.ChargeStateUnknownError:
        logger.error(
            "Charge outcome unknown: payment_id=%s customer_id=%s amount=%s",
            payment_id, payment.customer_id, payment.amount,
        )
        raise

    with get_connection() as conn:
        conn.execute(
            """INSERT INTO payments (id, amount, currency, customer_id, status, description, processor_id)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (
                payment_id,
                payment.amount,
                payment.currency.value,
                payment.customer_id,
                proc_result.status,
                payment.description,
                proc_result.processor_id,
            ),
        )
        if idempotency_key:
            conn.execute(
                "INSERT OR REPLACE INTO idempotency_keys (key, payment_id) VALUES (?, ?)",
                (idempotency_key, payment_id),
            )
        row = conn.execute(
            "SELECT * FROM payments WHERE id = ?", (payment_id,)
        ).fetchone()

    return _row_to_response(row), False


def _lookup_idempotency_key(key: str) -> Optional[PaymentResponse]:
    """Return the original PaymentResponse if the key exists and has not expired."""
    expiry = datetime.utcnow() - timedelta(hours=IDEMPOTENCY_KEY_TTL_HOURS)
    with get_connection() as conn:
        row = conn.execute(
            """SELECT payment_id FROM idempotency_keys
               WHERE key = ? AND created_at > ?""",
            (key, expiry.strftime("%Y-%m-%d %H:%M:%S")),
        ).fetchone()
    if not row:
        return None
    return get_payment(row["payment_id"])


def get_payment(payment_id: str) -> Optional[PaymentResponse]:
    with get_connection() as conn:
        row = conn.execute(
            "SELECT * FROM payments WHERE id = ?", (payment_id,)
        ).fetchone()
    return _row_to_response(row) if row else None


def list_payments(limit: int = 50) -> List[PaymentResponse]:
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM payments ORDER BY created_at DESC LIMIT ?", (limit,)
        ).fetchall()
    return [_row_to_response(r) for r in rows]


def _row_to_response(row) -> PaymentResponse:
    return PaymentResponse(
        id=row["id"],
        amount=row["amount"],
        currency=row["currency"],
        customer_id=row["customer_id"],
        status=row["status"],
        description=row["description"],
        created_at=str(row["created_at"]),
    )
