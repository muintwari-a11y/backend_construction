# Dashboard Backend API

A secure, lightweight FastAPI backend for dashboard applications using SQLite3.

## Features

- FastAPI with async support
- JWT-based authentication
- Role-based authorization (admin/user)
- SQLite database with SQLAlchemy ORM
- CORS support
- REST API endpoints for dashboard data
- Ready for Render deployment

## Local Development

### Prerequisites

- Python 3.9+
- pip

### Setup

1. Clone or navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Copy `.env` and update the values:
     ```
     SECRET_KEY=your-secret-key-here
     DATABASE_URL=sqlite:///./database.db
     JWT_SECRET_KEY=your-jwt-secret-key-here
     CORS_ORIGINS=http://localhost:3000,https://your-frontend-domain.com
     ACCESS_TOKEN_EXPIRE_MINUTES=30
     REFRESH_TOKEN_EXPIRE_DAYS=7
     ```

4. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Open your browser to `http://localhost:8000/docs` for API documentation.

## API Endpoints

### Authentication
- `POST /api/auth/login` - Login
- `POST /api/auth/register` - Register
- `POST /api/auth/refresh` - Refresh token

### Users
- `GET /api/users/me` - Get current user
- `GET /api/users/` - Get all users (admin only)

### Dashboard
- `GET /api/dashboard/summary` - Get dashboard summary
- `GET /api/dashboard/metrics` - Get dashboard metrics
- `GET /api/dashboard/activity` - Get recent activities

### Health
- `GET /api/health` - Health check

## Deployment on Render

1. Create a new Web Service on Render
2. Connect your repository
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Add environment variables in Render dashboard:
   - `SECRET_KEY`
   - `DATABASE_URL`
   - `JWT_SECRET_KEY`
   - `CORS_ORIGINS`
   - `ACCESS_TOKEN_EXPIRE_MINUTES`
   - `REFRESH_TOKEN_EXPIRE_DAYS`

## Database

The application uses SQLite3 with WAL mode enabled for better concurrency. Tables are automatically created on startup.

## Security

- Passwords hashed with bcrypt
- JWT tokens for authentication
- Role-based access control
- CORS protection
- SQL injection prevention via ORM