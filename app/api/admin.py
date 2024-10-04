from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.user import User, RoleEnum, StatusEnum
from app.db.session import get_db
from app.core.security import get_current_user

router = APIRouter()

@router.get("/admin/users/")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.post("/admin/users/")
def create_user(user: User, db: Session = Depends(get_db)):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.put("/admin/users/{user_id}/")
def update_user(user_id: str, status: StatusEnum, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.status = status
    db.commit()
    db.refresh(user)
    return user

@router.delete("/admin/users/{user_id}/")
def delete_user(user_id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted"}
