import uuid
from sqlalchemy import Column, String, Numeric, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.database import Base

class Asset(Base):
    __tablename__ = "assets"
    __table_args__ = (
        CheckConstraint("asset_type IN ('crypto', 'stock', 'gold', 'real_estate')", name="assets_asset_type_check"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    account_id = Column(UUID(as_uuid=True), ForeignKey("accounts.id"), nullable=False, index=True)
    name = Column(String, nullable=False)
    asset_type = Column(String, nullable=False)  # 'crypto', 'stock', 'gold', 'real_estate'
    quantity = Column(Numeric(19, 8), nullable=False, server_default="0")
    current_value = Column(Numeric(19, 4), nullable=False, server_default="0")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)