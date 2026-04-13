from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class Currency(str, Enum):
    USD = "usd"
    EUR = "eur"
    GBP = "gbp"


class PaymentStatus(str, Enum):
    PENDING = "pending"
    SUCCEEDED = "succeeded"
    FAILED = "failed"


class PaymentRequest(BaseModel):
    amount: int = Field(..., gt=0, description="Amount in cents")
    currency: Currency = Currency.USD
    customer_id: str
    description: Optional[str] = None


class PaymentResponse(BaseModel):
    id: str
    amount: int
    currency: str
    customer_id: str
    status: str
    description: Optional[str]
    created_at: str


class ProcessorResponse(BaseModel):
    processor_id: str
    status: str
    amount: int
    currency: str
