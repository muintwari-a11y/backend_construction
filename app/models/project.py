from sqlalchemy import Column, Integer, String, Text, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    status = Column(String, default="planning")  # planning, in_progress, completed, on_hold
    progress = Column(Float, default=0.0)  # 0-100
    start_date = Column(DateTime(timezone=True))
    end_date = Column(DateTime(timezone=True))
    budget = Column(Float)
    location = Column(String)
    client_name = Column(String)
    client_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    created_by_id = Column(Integer, ForeignKey("users.id"))
    created_by = relationship("User", back_populates="projects", foreign_keys=[created_by_id])
    client = relationship("User", back_populates="client_projects", foreign_keys=[client_id])
    transactions = relationship("Transaction", back_populates="project")
    messages = relationship("Message", back_populates="project")