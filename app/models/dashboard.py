from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class DashboardMetric(Base):
    __tablename__ = "dashboard_metrics"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    value = Column(String)
    category = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())