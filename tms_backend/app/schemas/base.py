import uuid

from datetime import datetime

from pydantic import BaseModel
from pydantic.config import ConfigDict


class ORMBaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class BaseReadSchema(ORMBaseSchema):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    created_by: uuid.UUID | None = None
    updated_by: uuid.UUID | None = None