from decouple import config

class Settings:
    SECRET_KEY: str = config("SECRET_KEY")
    DATABASE_URL: str = config("DATABASE_URL")
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY")
    CORS_ORIGINS: list = config("CORS_ORIGINS", default="http://localhost:3000").split(",")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = config("ACCESS_TOKEN_EXPIRE_MINUTES", default=30, cast=int)
    REFRESH_TOKEN_EXPIRE_DAYS: int = config("REFRESH_TOKEN_EXPIRE_DAYS", default=7, cast=int)

    # Email settings
    SMTP_SERVER: str = config("SMTP_SERVER", default="smtp.gmail.com")
    SMTP_PORT: int = config("SMTP_PORT", default=587, cast=int)
    SMTP_USERNAME: str = config("SMTP_USERNAME", default="")
    SMTP_PASSWORD: str = config("SMTP_PASSWORD", default="")
    EMAIL_FROM: str = config("EMAIL_FROM", default="noreply@goconstructionltd.com")
    EMAIL_TO: str = config("EMAIL_TO", default="it@goconstructionltd.com")

settings = Settings()