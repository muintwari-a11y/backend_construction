#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.core.database import SessionLocal, create_tables
from app.core.security import get_password_hash
from app.models.user import User
from app.models.project import Project
from app.models.transaction import Transaction
from app.models.message import Message
from app.models.activity import Activity

def add_test_user():
    db = SessionLocal()
    try:
        # Check if user already exists
        existing_user = db.query(User).filter(User.email == "admin@goconstruction.rw").first()
        if existing_user:
            print(f"Test user already exists: {existing_user.email}, id: {existing_user.id}")
            return

        # Create test user
        hashed_password = get_password_hash("admin123")
        test_user = User(
            email="admin@goconstruction.rw",
            password_hash=hashed_password,
            name="Admin User",
            role="admin"
        )
        db.add(test_user)
        db.commit()
        db.refresh(test_user)
        print(f"Test user created: {test_user.email} / admin123, id: {test_user.id}")
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_test_user()