from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    role: str = "user"

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