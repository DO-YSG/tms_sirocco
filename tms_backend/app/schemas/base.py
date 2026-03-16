import uuid

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ORMBaseSchema(BaseModel):
    class Config:
        from_attributes = True

class BaseRaedSchema(ORMBaseSchema):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    created_by: Optional[uuid.UUID] = None
    updated_by: Optional[uuid.UUID] = None