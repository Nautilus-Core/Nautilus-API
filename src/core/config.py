# Desc: Load environment variables from .env file
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "🌊 Nautilus API"
    PROJECT_DESC: str = "A API for studying the seas."
    VERSION: str = "0.1.0"
    API_PREFIX: str = "/api/v1"


    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    # Security settings
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 # 1 hour


config = Settings()