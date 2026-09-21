from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
from uuid import UUID
from typing import Optional

class GoalContributionCreate(BaseModel):
    amount: Decimal
    source: Optional[str] = None

class GoalContributionOut(BaseModel):
    id: UUID
    goal_id: UUID
    amount: Decimal
    source: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True