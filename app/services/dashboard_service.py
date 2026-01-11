from sqlalchemy.orm import Session
from app.models.user import User
from app.models.dashboard import DashboardMetric
from app.models.activity import Activity

def get_summary(db: Session):
    total_users = db.query(User).count()
    total_metrics = db.query(DashboardMetric).count()
    activities = db.query(Activity).order_by(Activity.timestamp.desc()).limit(10).all()
    return {
        "total_users": total_users,
        "total_metrics": total_metrics,
        "recent_activities": [{"action": a.action, "timestamp": str(a.timestamp)} for a in activities]
    }

def get_metrics(db: Session):
    return db.query(DashboardMetric).all()

def get_activities(db: Session):
    activities = db.query(Activity).all()
    return [{"action": a.action, "timestamp": str(a.timestamp)} for a in activities]