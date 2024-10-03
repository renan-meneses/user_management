from sqlalchemy import Column, String, Enum, Boolean, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db.base import Base
from enum import Enum as PyEnum

class RoleEnum(PyEnum):
    admin = "admin"
    user = "user"

class StatusEnum(PyEnum):
    active = "active"
    inactive = "inactive"

class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    role = Column(Enum(RoleEnum), default=RoleEnum.user, nullable=False)
    status = Column(Enum(StatusEnum), default=StatusEnum.active, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())
