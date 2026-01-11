import json
import os
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.core.security import decode_token

# Load users from JSON
USERS_FILE = os.path.join(os.path.dirname(__file__), '..', '..', 'users.json')
with open(USERS_FILE, 'r') as f:
    users_db = json.load(f)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = decode_token(token)
    if payload is None:
        raise credentials_exception
    email: str = payload.get("sub")
    if email is None:
        raise credentials_exception
    user = next((u for u in users_db if u['email'] == email), None)
    if user is None:
        raise credentials_exception
    return user

def get_current_active_user(current_user: dict = Depends(get_current_user)):
    if not current_user.get('is_active', True):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def get_admin_user(current_user: dict = Depends(get_current_active_user)):
    if current_user.get('role') != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return current_user