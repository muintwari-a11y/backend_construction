from sqlalchemy.orm import Session
from app.core.security import verify_password, get_password_hash
from app.models.user import User

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password_hash):
        return False
    return user

def create_user(db: Session, email: str, password: str, role: str = "user"):
    hashed_password = get_password_hash(password)
    new_user = User(email=email, password_hash=hashed_password, role=role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user