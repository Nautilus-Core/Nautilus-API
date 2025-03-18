from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..core.config import config

DATABASE_URL = config.DATABASE_URL.replace("postgresql://", "postgresql+psycopg://")

engine = create_engine(DATABASE_URL, connect_args={"client_encoding": "utf8"})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
