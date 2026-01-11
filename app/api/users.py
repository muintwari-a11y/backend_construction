from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user import User
from app.schemas.user import User
from app.api.deps import get_current_active_user, get_admin_user

router = APIRouter()

@router.get("/me", response_model=User)
def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@router.get("/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: User = Depends(get_admin_user)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users