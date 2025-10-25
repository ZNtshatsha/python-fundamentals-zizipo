from typing import Optional

from sqlalchemy.orm import Session

from .models import User


def create_user(db: Session, name: str, email: str, age: int) -> User:
    user = User(name=name, email=email, age=age)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()
