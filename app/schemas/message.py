from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MessageBase(BaseModel):
    subject: str
    content: str
    message_type: str = "general"
    service_type: Optional[str] = None
    recipient_id: int
    project_id: Optional[int] = None

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    id: int
    sender_id: int
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True

class MessageWithUsers(Message):
    sender_name: str
    recipient_name: str