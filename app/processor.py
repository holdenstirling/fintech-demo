"""
External payment processor integration.
FinTechCo uses a third-party processor for card authorization and settlement.
"""
import uuid
import httpx
from app.config import PROCESSOR_API_KEY, PROCESSOR_BASE_URL
from app.models import ProcessorResponse


class ChargeRejectedError(Exception):
    """Charge definitively rejected by the processor (4xx)."""


class ChargeStateUnknownError(Exception):
    """Charge outcome unknown — timeout, 5xx, or connection error."""


def charge(amount: int, currency: str, customer_id: str, idempotency_key: str) -> ProcessorResponse:
    """
    Submit a charge to the external payment processor.

    In production this calls the real processor API. For the demo
    environment we simulate the response without a live network call.
    """
    # Simulate the outbound API call structure so the code is realistic
    payload = {
        "amount": amount,
        "currency": currency,
        "customer": customer_id,
        "capture_method": "automatic",
    }
    headers = {
        "Authorization": f"Bearer {PROCESSOR_API_KEY}",
        "Content-Type": "application/json",
        "Idempotency-Key": idempotency_key,
    }

    # --- Real call (commented out to avoid live network in demo) ---
    # try:
    #     response = httpx.post(
    #         f"{PROCESSOR_BASE_URL}/charges",
    #         json=payload,
    #         headers=headers,
    #         timeout=10.0,
    #     )
    #     response.raise_for_status()
    #     data = response.json()
    # except httpx.HTTPStatusError as e:
    #     if e.response.status_code < 500:
    #         raise ChargeRejectedError(f"Processor rejected: {e.response.status_code}") from e
    #     raise ChargeStateUnknownError(f"Processor error: {e.response.status_code}") from e
    # except (httpx.TimeoutException, httpx.ConnectError) as e:
    #     raise ChargeStateUnknownError(f"Processor unreachable: {e}") from e

    # Simulated success response
    data = {
        "processor_id": f"proc_{uuid.uuid4().hex[:16]}",
        "status": "succeeded",
        "amount": amount,
        "currency": currency,
    }

    return ProcessorResponse(**data)
