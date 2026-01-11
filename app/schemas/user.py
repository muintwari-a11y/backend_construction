from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    email: str
    name: Optional[str] = None
    role: str = "user"
    staff_id: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    created_at: str

    class Config:
        from_attributes = True

class UserInDB(User):
    password_hash: str