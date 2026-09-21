from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.database import get_db
from app.models.transaction import Transaction
from app.models.account import Account
from app.models.user import User
from app.schemas.transaction import TransactionCreate, TransactionOut
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/transactions", tags=["transactions"])

def _verify_account_ownership(db: Session, account_id: UUID, user_id: UUID):
    account = db.query(Account).filter(Account.id == account_id, Account.user_id == user_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")

@router.post("/", response_model=TransactionOut, status_code=201)
def create_transaction(payload: TransactionCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    _verify_account_ownership(db, payload.account_id, current_user.id)
    transaction = Transaction(**payload.model_dump(exclude_unset=True))
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction

@router.get("/", response_model=list[TransactionOut])
def list_transactions(account_id: UUID, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    _verify_account_ownership(db, account_id, current_user.id)
    return db.query(Transaction).filter(Transaction.account_id == account_id).all()

@router.get("/{transaction_id}", response_model=TransactionOut)
def get_transaction(transaction_id: UUID, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    transaction = db.query(Transaction).join(Account).filter(
        Transaction.id == transaction_id, Account.user_id == current_user.id
    ).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@router.delete("/{transaction_id}", status_code=204)
def delete_transaction(transaction_id: UUID, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    transaction = db.query(Transaction).join(Account).filter(
        Transaction.id == transaction_id, Account.user_id == current_user.id
    ).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    db.delete(transaction)
    db.commit()