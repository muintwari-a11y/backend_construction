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

# Staff data for creating users
staff_data = [
    {"id": "chairman", "email": "chairman@goconstruction.rw", "name": "Eng. Nkurunziza Gilbert", "role": "admin"},
    {"id": "md", "email": "md@goconstruction.rw", "name": "Eng. Nsengimana Olivier", "role": "admin"},
    {"id": "td", "email": "td@goconstruction.rw", "name": "Eng. Izere Aime Bruce", "role": "admin"},
    {"id": "ad", "email": "ad@goconstruction.rw", "name": "Nkurikiyintwari Donath", "role": "financial"},
    {"id": "accountant", "email": "accountant@goconstruction.rw", "name": "Tuyishimire Divine", "role": "financial"},
    {"id": "qe", "email": "qe@goconstruction.rw", "name": "Eng. Mbarushimana Tharcisse", "role": "staff"},
    {"id": "pm", "email": "pm@goconstruction.rw", "name": "Eng. Manzi Bizimungu Aubin", "role": "staff"},
    {"id": "arch", "email": "arch@goconstruction.rw", "name": "Eng. Niyonsenga Roger", "role": "staff"},
    {"id": "qs", "email": "qs@goconstruction.rw", "name": "Eng. Ineza Robert", "role": "staff"},
    {"id": "water", "email": "water@goconstruction.rw", "name": "Eng. Tuyizere Alexandre", "role": "staff"},
    {"id": "geo", "email": "geo@goconstruction.rw", "name": "Eng. Nshimyimana Aime Valantin", "role": "staff"},
    {"id": "env", "email": "env@goconstruction.rw", "name": "Eng. Manzi Malyse", "role": "staff"},
    {"id": "ele", "email": "ele@goconstruction.rw", "name": "Maitre Eng. Mugemana Miguel", "role": "staff"},
    {"id": "it1", "email": "it@goconstruction.rw", "name": "IT. Mugenga Ntwari Olivier", "role": "admin"},
    {"id": "media", "email": "media@goconstruction.rw", "name": "IT. Nayituriki Olivier", "role": "staff"},
    {"id": "eng1", "email": "eng1@goconstruction.rw", "name": "Eng. Ndatimana Regis", "role": "staff"},
    {"id": "eng2", "email": "eng2@goconstruction.rw", "name": "Eng. Dukundane Anselme", "role": "staff"},
    {"id": "eng3", "email": "eng3@goconstruction.rw", "name": "Eng. Impano Aime Fiacre", "role": "staff"},
    {"id": "eng4", "email": "eng4@goconstruction.rw", "name": "Eng. Kandangira Hubert", "role": "staff"},
    {"id": "eng5", "email": "eng5@goconstruction.rw", "name": "Maitre Eng. Mukamisha Barbara", "role": "staff"},
    {"id": "eng6", "email": "eng6@goconstruction.rw", "name": "Eng. Nyabyenda Paulin", "role": "staff"},
]

def add_staff_users():
    db = SessionLocal()
    try:
        for staff in staff_data:
            # Check if user already exists
            existing_user = db.query(User).filter(User.email == staff["email"]).first()
            if existing_user:
                print(f"User already exists: {existing_user.email}")
                continue

            # Create user
            hashed_password = get_password_hash("staff123")  # Default password for all staff
            new_user = User(
                email=staff["email"],
                password_hash=hashed_password,
                name=staff["name"],
                role=staff["role"],
                staff_id=staff["id"]
            )
            db.add(new_user)
            print(f"Created user: {staff['email']} / staff123")
        
        db.commit()
        print("All staff users created successfully")
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_staff_users()