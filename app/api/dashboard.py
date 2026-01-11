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
    # Role-based dashboard data
    if current_user.role == "client":
        # Client dashboard: focus on their projects and services
        client_projects = db.query(Project).filter(Project.client_id == current_user.id).count()
        active_services = 4  # Placeholder for services they're using
        recent_updates = db.query(Activity).filter(
            Activity.user_id == current_user.id
        ).order_by(Activity.timestamp.desc()).limit(3).all()

        return {
            "stats": {
                "my_projects": client_projects,
                "active_services": active_services,
                "support_tickets": 2,  # Placeholder
                "next_milestone": "Foundation completion - 2 weeks"
            },
            "recent_activities": [
                {
                    "action": a.action,
                    "timestamp": str(a.timestamp),
                    "time_ago": "Recently"
                } for a in recent_updates
            ],
            "quick_actions": [
                {"label": "My Projects", "href": "/dashboard/projects"},
                {"label": "Request Service", "href": "/dashboard/services"},
                {"label": "Contact Support", "href": "/dashboard/support"},
                {"label": "Schedule Meeting", "href": "/dashboard/schedule"}
            ]
        }
    elif current_user.role in ["admin", "staff", "financial"]:
        # Staff/Admin dashboard
        total_users = db.query(User).count()
        active_projects = db.query(Project).count()  # Use actual count
        team_members = db.query(User).filter(User.role.in_(["admin", "staff", "financial"])).count()
        monthly_revenue = "RWF 45M"  # Placeholder

        # Get recent activities
        activities = db.query(Activity).order_by(Activity.timestamp.desc()).limit(5).all()
        recent_activities = [
            {
                "action": a.action,
                "timestamp": str(a.timestamp),
                "time_ago": "2 hours ago"
            } for a in activities
        ]

        quick_actions = []
        if current_user.role == "admin":
            quick_actions = [
                {"label": "Team Management", "href": "/dashboard/team"},
                {"label": "Projects", "href": "/dashboard/projects"},
                {"label": "Financial", "href": "/dashboard/financial"},
                {"label": "Reports", "href": "/dashboard/reports"}
            ]
        elif current_user.role == "financial":
            quick_actions = [
                {"label": "Financial Overview", "href": "/dashboard/financial"},
                {"label": "Transactions", "href": "/dashboard/transactions"},
                {"label": "Reports", "href": "/dashboard/reports"},
                {"label": "Budget Planning", "href": "/dashboard/budget"}
            ]
        else:  # staff
            quick_actions = [
                {"label": "My Projects", "href": "/dashboard/projects"},
                {"label": "Department Tasks", "href": "/dashboard/tasks"},
                {"label": "Team Communication", "href": "/dashboard/communication"},
                {"label": "Schedule Meeting", "href": "/dashboard/schedule"}
            ]

        return {
            "stats": {
                "active_projects": active_projects,
                "team_members": team_members,
                "achievements": 5,
                "monthly_revenue": monthly_revenue
            },
            "recent_activities": recent_activities,
            "quick_actions": quick_actions
        }
    else:
        # Default fallback
        return {
            "stats": {"message": "Dashboard not configured for this role"},
            "recent_activities": [],
            "quick_actions": []
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