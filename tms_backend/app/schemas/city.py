import uuid
from pydantic import BaseModel, Field
from typing import Optional


class CityBase(BaseModel):
    name: str = Field(..., max_length=50)
    region: str = Field(..., max_length=50)
    country: str = Field(..., max_length=50)

class CityCreate(CityBase):
    pass

class CityUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=50)
    region: Optional[str] = Field(None, max_length=50)
    country: Optional[str] = Field(None, max_length=50)

class CityRead(CityBase):
    id: uuid.UUID
    
    class Config:
        from_attributes = True