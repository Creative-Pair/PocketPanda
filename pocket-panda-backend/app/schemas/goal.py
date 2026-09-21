from pydantic import BaseModel
from datetime import datetime, date
from decimal import Decimal
from uuid import UUID
from typing import Optional

class GoalCreate(BaseModel):
    name: str
    target_amount: Decimal
    deadline: Optional[date] = None

class GoalUpdate(BaseModel):
    name: Optional[str] = None
    target_amount: Optional[Decimal] = None
    deadline: Optional[date] = None

class GoalOut(BaseModel):
    id: UUID
    user_id: UUID
    name: str
    target_amount: Decimal
    current_amount: Decimal
    deadline: Optional[date]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True