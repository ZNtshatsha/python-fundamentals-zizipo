from sqlalchemy.orm import Session
from models import User

def get_all_users(db: Session):
    return db.query(User).all()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, username: str, email: str, age: int):
    try:
        new_user = User(username=username, email=email, age=age)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
        return None

def update_user_age(db: Session, username: str, new_age: int):
    user = db.query(User).filter(User.username == username).first()
    if user:
        user.age = new_age
        db.commit()
        db.refresh(user)
        return user
    return None
