from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base

metadata = MetaData()
Base = declarative_base()

# --- Using SQLAlchemy Table (Core)
users_table = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String(100), unique=True, nullable=False),
    Column('email', String(100), nullable=False),
    Column('age', Integer)
)

# --- Using ORM Model (Declarative)
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(100), nullable=False)
    age = Column(Integer)
from database import engine

Base.metadata.create_all(bind=engine)
