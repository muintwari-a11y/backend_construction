from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user import User
from app.models.dashboard import DashboardMetric
from app.models.activity import Activity
from app.schemas.dashboard import DashboardSummary, DashboardMetric as DashboardMetricSchema, ActivityBase
from app.api.deps import get_current_active_user

router = APIRouter()

@router.get("/summary", response_model=DashboardSummary)
def get_dashboard_summary(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    total_users = db.query(User).count()
    total_metrics = db.query(DashboardMetric).count()
    activities = db.query(Activity).order_by(Activity.timestamp.desc()).limit(10).all()
    recent_activities = [{"action": a.action, "timestamp": str(a.timestamp)} for a in activities]
    return {"total_users": total_users, "total_metrics": total_metrics, "recent_activities": recent_activities}

@router.get("/metrics", response_model=List[DashboardMetricSchema])
def get_dashboard_metrics(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    metrics = db.query(DashboardMetric).all()
    return metrics

@router.get("/activity", response_model=List[ActivityBase])
def get_dashboard_activity(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    activities = db.query(Activity).all()
    return [{"action": a.action, "timestamp": str(a.timestamp)} for a in activities]