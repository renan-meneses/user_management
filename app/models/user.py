from sqlalchemy import Column, String, Enum, func
from app.utils.base_model import BaseModel
from enum import Enum as PyEnum
class RoleEnum(PyEnum):
    admin = "admin"
    user = "user"

class StatusEnum(PyEnum):
    active = "active"
    inactive = "inactive"

class User(BaseModel):
    __tablename__ = "users"
    
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    role = Column(Enum(RoleEnum), default=RoleEnum.user, nullable=False)
    status = Column(Enum(StatusEnum), default=StatusEnum.active, nullable=False)
