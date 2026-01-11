from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user import User
from app.models.message import Message
from app.schemas.message import MessageCreate, Message, MessageWithUsers
from app.api.deps import get_current_active_user

router = APIRouter()

@router.post("/", response_model=Message)
def send_message(
    message: MessageCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    # Check if recipient exists
    recipient = db.query(User).filter(User.id == message.recipient_id).first()
    if not recipient:
        raise HTTPException(status_code=404, detail="Recipient not found")

    # Create message
    db_message = Message(
        subject=message.subject,
        content=message.content,
        message_type=message.message_type,
        service_type=message.service_type,
        sender_id=current_user.id,
        recipient_id=message.recipient_id,
        project_id=message.project_id
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

@router.get("/sent", response_model=List[MessageWithUsers])
def get_sent_messages(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    messages = db.query(Message).filter(Message.sender_id == current_user.id).all()
    result = []
    for msg in messages:
        result.append({
            **msg.__dict__,
            "sender_name": msg.sender.name,
            "recipient_name": msg.recipient.name
        })
    return result

@router.get("/received", response_model=List[MessageWithUsers])
def get_received_messages(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    messages = db.query(Message).filter(Message.recipient_id == current_user.id).all()
    result = []
    for msg in messages:
        result.append({
            **msg.__dict__,
            "sender_name": msg.sender.name,
            "recipient_name": msg.recipient.name
        })
    return result

@router.put("/{message_id}/read")
def mark_message_read(
    message_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    message = db.query(Message).filter(
        Message.id == message_id,
        Message.recipient_id == current_user.id
    ).first()
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")

    message.is_read = True
    db.commit()
    return {"message": "Message marked as read"}

@router.get("/staff-by-service/{service_type}")
def get_staff_by_service(
    service_type: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    # Map service types to roles
    role_mapping = {
        "engineering": ["staff"],
        "financial": ["financial"],
        "management": ["admin"],
        "technical": ["staff"],
    }

    roles = role_mapping.get(service_type, ["staff"])
    staff = db.query(User).filter(
        User.role.in_(roles),
        User.is_active == True
    ).all()

    return [{"id": s.id, "name": s.name, "role": s.role} for s in staff]