import json
import os
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import verify_password, get_password_hash, create_access_token, decode_token
from app.models.user import User
from app.schemas.auth import UserLogin, Token, RefreshToken
from app.schemas.user import UserCreate, User as UserSchema
from app.api.deps import get_current_active_user

# Load users from JSON
USERS_FILE = os.path.join(os.path.dirname(__file__), '..', '..', 'users.json')
with open(USERS_FILE, 'r') as f:
    users_db = json.load(f)

router = APIRouter()

@router.post("/login", response_model=Token)
def login(user_credentials: UserLogin):
    user = next((u for u in users_db if u['email'] == user_credentials.email), None)
    if not user or user_credentials.password != "staff123":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user['email']})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=Token)
def register(user: UserCreate):
    # For demo, registration is disabled
    raise HTTPException(status_code=400, detail="Registration is disabled for demo")

@router.get("/me", response_model=UserSchema)
def get_current_user(current_user: dict = Depends(get_current_active_user)):
    return current_user

@router.post("/refresh", response_model=Token)
def refresh_token(refresh: RefreshToken):
    payload = decode_token(refresh.refresh_token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    email = payload.get("sub")
    access_token = create_access_token(data={"sub": email})
    return {"access_token": access_token, "token_type": "bearer"}