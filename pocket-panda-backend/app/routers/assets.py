from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.database import get_db
from app.models.asset import Asset
from app.models.account import Account
from app.models.user import User
from app.schemas.asset import AssetCreate, AssetOut
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/assets", tags=["assets"])

def _verify_account_ownership(db: Session, account_id: UUID, user_id: UUID):
    account = db.query(Account).filter(Account.id == account_id, Account.user_id == user_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")

@router.post("/", response_model=AssetOut, status_code=201)
def create_asset(payload: AssetCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    _verify_account_ownership(db, payload.account_id, current_user.id)
    asset = Asset(**payload.model_dump())
    db.add(asset)
    db.commit()
    db.refresh(asset)
    return asset

@router.get("/", response_model=list[AssetOut])
def list_assets(account_id: UUID, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    _verify_account_ownership(db, account_id, current_user.id)
    return db.query(Asset).filter(Asset.account_id == account_id).all()

@router.put("/{asset_id}", response_model=AssetOut)
def update_asset(asset_id: UUID, payload: AssetCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    asset = db.query(Asset).join(Account).filter(Asset.id == asset_id, Account.user_id == current_user.id).first()
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    for field, value in payload.model_dump().items():
        setattr(asset, field, value)
    db.commit()
    db.refresh(asset)
    return asset

@router.delete("/{asset_id}", status_code=204)
def delete_asset(asset_id: UUID, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    asset = db.query(Asset).join(Account).filter(Asset.id == asset_id, Account.user_id == current_user.id).first()
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    db.delete(asset)
    db.commit()