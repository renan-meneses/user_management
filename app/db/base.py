from sqlalchemy.orm import declarative_base

Base = declarative_base()

from app.models.user import User  # Adicione outros modelos conforme necessário

