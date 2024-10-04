import datetime
from unittest.mock import Base
from sqlalchemy import Column, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import UUID
import uuid

class BaseModel(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())
    
    class Meta:
        abstract = True
        
    def save(self, *args, **kwargs):
        self.updated_at = datetime.timezone.now()  # Corrigido de 'update_at' para 'updated_at'
        super().save(*args, **kwargs)