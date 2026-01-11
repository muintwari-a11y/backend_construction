from typing import List, Dict, Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user import User
from app.models.dashboard import DashboardMetric
from app.models.activity import Activity
from app.schemas.dashboard import DashboardSummary, DashboardMetric as DashboardMetricSchema, ActivityBase
from app.api.deps import get_current_active_user

router = APIRouter()

@router.get("", response_model=Dict[str, Any])
def get_dashboard_data(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    # Get basic stats
    total_users = db.query(User).count()
    active_projects = 12  # Placeholder, should come from projects model
    team_members = total_users  # Assuming all users are team members
    monthly_revenue = "RWF 45M"  # Placeholder

    # Get recent activities
    activities = db.query(Activity).order_by(Activity.timestamp.desc()).limit(5).all()
    recent_activities = [
        {
            "action": a.action,
            "timestamp": str(a.timestamp),
            "time_ago": "2 hours ago"  # Placeholder, calculate properly
        } for a in activities
    ]

    return {
        "stats": {
            "active_projects": active_projects,
            "team_members": team_members,
            "achievements": 5,  # Placeholder
            "monthly_revenue": monthly_revenue
        },
        "recent_activities": recent_activities,
        "quick_actions": [
            {"label": "Projects", "href": "/dashboard/projects"},
            {"label": "Financial", "href": "/dashboard/financial"},
            {"label": "Achievements", "href": "/dashboard/achievements"},
            {"label": "Schedule Meeting", "href": "/dashboard/schedule"}
        ]
    }

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