from pydantic import BaseModel
from datetime import datetime, date
from decimal import Decimal
from uuid import UUID
from typing import Optional

class TransactionCreate(BaseModel):
    account_id: UUID
    category_id: Optional[UUID] = None
    type: str  # 'expense' or 'investment'
    amount: Decimal
    note: Optional[str] = None
    transaction_date: Optional[date] = None

class TransactionOut(BaseModel):
    id: UUID
    account_id: UUID
    category_id: Optional[UUID]
    type: str
    amount: Decimal
    note: Optional[str]
    transaction_date: date
    voided_at: Optional[datetime]
    created_at: datetime

    class Config:
        from_attributes = True