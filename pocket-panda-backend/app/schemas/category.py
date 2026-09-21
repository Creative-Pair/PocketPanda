from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class CategoryCreate(BaseModel):
    name: str
    type: str  # 'expense' or 'investment'
    is_global: bool = True

class CategoryOut(BaseModel):
    id: UUID
    name: str
    type: str
    is_global: bool
    created_at: datetime

    class Config:
        from_attributes = True