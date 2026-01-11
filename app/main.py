from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api import auth, users, dashboard, health, company, projects, transactions, contact, messages

app = FastAPI(title="Go Construction API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8081", "http://localhost:5173", "http://localhost:3000", "https://goconstructioltd.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
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
app.include_router(messages.router, prefix="/messages", tags=["messages"])

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# No startup event needed for JSON-based backend

if __name__ == "__main__":
    import os
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)