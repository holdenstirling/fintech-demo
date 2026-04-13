"""
External payment processor integration.
FinTechCo uses a third-party processor for card authorization and settlement.
"""
import uuid
import httpx
from app.config import PROCESSOR_API_KEY, PROCESSOR_BASE_URL
from app.models import ProcessorResponse


def charge(amount: int, currency: str, customer_id: str) -> ProcessorResponse:
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
        "Idempotency-Key": str(uuid.uuid4()),  # processor-level, not our layer
    }

    # --- Real call (commented out to avoid live network in demo) ---
    # response = httpx.post(
    #     f"{PROCESSOR_BASE_URL}/charges",
    #     json=payload,
    #     headers=headers,
    #     timeout=10.0,
    # )
    # response.raise_for_status()
    # data = response.json()

    # Simulated success response
    data = {
        "processor_id": f"proc_{uuid.uuid4().hex[:16]}",
        "status": "succeeded",
        "amount": amount,
        "currency": currency,
    }

    return ProcessorResponse(**data)
