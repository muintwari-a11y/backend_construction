from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.database import create_tables
from app.api import auth, users, dashboard, health, company, projects, transactions, contact

app = FastAPI(title="Go Construction API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
app.include_router(health.router, prefix="", tags=["health"])
app.include_router(company.router, prefix="/company", tags=["company"])
app.include_router(projects.router, prefix="/projects", tags=["projects"])
app.include_router(transactions.router, prefix="/transactions", tags=["transactions"])
app.include_router(contact.router, prefix="/contact", tags=["contact"])

@app.on_event("startup")
def startup_event():
    create_tables()