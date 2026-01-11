from sqlalchemy import Column, Integer, String, Text, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)  # income, expense
    category = Column(String, nullable=False)  # materials, labor, equipment, etc.
    amount = Column(Float, nullable=False)
    description = Column(Text)
    date = Column(DateTime(timezone=True), server_default=func.now())
    reference = Column(String)  # invoice number, receipt, etc.
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    created_by_id = Column(Integer, ForeignKey("users.id"))
    created_by = relationship("User", back_populates="transactions")

    project_id = Column(Integer, ForeignKey("projects.id"), nullable=True)
    project = relationship("Project", back_populates="transactions")