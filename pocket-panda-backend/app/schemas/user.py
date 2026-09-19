from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# Shared base fields
class UserBase(BaseModel):
    full_name: str
    email: EmailStr

# What the client sends when signing up
class UserCreate(UserBase):
    password: str

# What the client sends when logging in
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# What the API returns (never includes the password)
class UserOut(UserBase):
    id: int
    is_active: bool
    is_verified: bool
    created_at: datetime

    class Config:
        from_attributes = True