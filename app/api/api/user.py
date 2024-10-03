from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.user import User
from app.db.session import get_db
from app.core.security import get_current_user

router = APIRouter()

@router.get("/user/profile/")
def get_profile(current_user: User = Depends(get_current_user)):
    return current_user

@router.put("/user/profile/")
def update_profile(name: str, email: str, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    current_user.name = name
    current_user.email = email
    db.commit()
    db.refresh(current_user)
    return current_user
