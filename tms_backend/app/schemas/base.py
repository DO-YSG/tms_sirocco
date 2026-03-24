import uuid

from pydantic import BaseModel
from pydantic.config import ConfigDict
from typing import Optional
from datetime import datetime

class ORMBaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class BaseReadSchema(ORMBaseSchema):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    created_by: Optional[uuid.UUID] = None
    updated_by: Optional[uuid.UUID] = None