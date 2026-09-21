from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
from uuid import UUID

class AssetCreate(BaseModel):
    account_id: UUID
    name: str
    asset_type: str  # 'crypto', 'stock', 'gold', 'real_estate'
    quantity: Decimal = Decimal("0")
    current_value: Decimal = Decimal("0")

class AssetOut(BaseModel):
    id: UUID
    account_id: UUID
    name: str
    asset_type: str
    quantity: Decimal
    current_value: Decimal
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True