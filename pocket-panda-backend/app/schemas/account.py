from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class AccountCreate(BaseModel):
    name: str = "Main Account"

class AccountOut(BaseModel):
    id: UUID
    user_id: UUID
    name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True