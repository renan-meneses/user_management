from fastapi import FastAPI
from app.api import auth, admin, user

app = FastAPI()

app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "API is running"}
