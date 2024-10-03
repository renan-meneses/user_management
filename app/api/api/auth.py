from fastapi import APIRouter, HTTPException
from app.core.security import cognito_authentication

router = APIRouter()

@router.post("/auth/login/")
def login(token: str):
    user = cognito_authentication(token)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid token")
    return {"message": "Logged in"}

@router.post("/auth/logout/")
def logout():
    return {"message": "Logged out"}
