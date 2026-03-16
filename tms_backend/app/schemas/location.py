import uuid

from pydantic import BaseModel, Field
from typing import Optional

from app.models.location import LocationType


class LocationBase(BaseModel):
    name: str = Field(..., max_length=100)
    location_type: LocationType
    city_id: uuid.UUID
    address_line: Optional[str] = Field(None, max_length=200)
    comment: Optional[str] = Field(None, max_length=300)

class LocationCreate(LocationBase):
    pass

class LocationUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    location_type: Optional[LocationType]  = None
    city_id: Optional[uuid.UUID] = None
    address_line: Optional[str] = Field(None, max_length=200)
    comment: Optional[str] = Field(None, max_length=300)

class LocationRead(LocationBase):
    id: uuid.UUID
    
    class Config:
        from_attributes = True