from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLAlchemy Base
Base = declarative_base()

# Database URL
DATABASE_URL = "mariadb+pymysql://appuser:apppassword@localhost:3306/users_db"

# Engine
engine = create_engine(
    DATABASE_URL,
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=1800
)

# Session factory
SessionLocal = sessionmaker(bind=engine)
