from pydantic import BaseModel
from typing import List

class DashboardMetricBase(BaseModel):
    title: str
    value: str
    category: str

class DashboardMetric(DashboardMetricBase):
    id: int
    created_at: str

    class Config:
        from_attributes = True

class ActivityBase(BaseModel):
    action: str
    timestamp: str

class DashboardSummary(BaseModel):
    total_users: int
    total_metrics: int
    recent_activities: List[ActivityBase]