"""
Core payment processing logic.

NOTE: This module does not implement idempotency keys. If a client submits
the same payment request twice (e.g. due to a network timeout and retry),
two separate charges will be created. See ISSUE.md for the open ticket.
"""
import uuid
from typing import List, Optional
from app.database import get_connection
from app.models import PaymentRequest, PaymentResponse
from app import processor


def create_payment(payment: PaymentRequest) -> PaymentResponse:
    """Process a payment: charge the processor, persist the record, return the result."""
    proc_result = processor.charge(
        amount=payment.amount,
        currency=payment.currency.value,
        customer_id=payment.customer_id,
    )

    payment_id = str(uuid.uuid4())

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
        row = conn.execute(
            "SELECT * FROM payments WHERE id = ?", (payment_id,)
        ).fetchone()

    return _row_to_response(row)


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
