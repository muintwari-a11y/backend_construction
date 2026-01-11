from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TransactionBase(BaseModel):
    type: str  # income, expense
    category: str
    amount: float
    description: Optional[str] = None
    date: Optional[datetime] = None
    reference: Optional[str] = None
    project_id: Optional[int] = None

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    created_at: datetime
    created_by_id: int

    class Config:
        from_attributes = True