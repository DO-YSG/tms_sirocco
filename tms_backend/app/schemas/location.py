import uuid

from pydantic import Field, model_validator

from app.schemas.base import ORMBaseSchema, BaseReadSchema
from app.models.enums import LocationType


class LocationBase(ORMBaseSchema):
    name: str = Field(..., max_length=255)
    location_type: LocationType
    location_type_custom: str | None = None
    address_line: str | None = Field(None, max_length=510)
    note: str | None = None

    @model_validator(mode="after")
    def validator_location_type(self):
        if self.location_type == LocationType.other and not self.location_type_custom:
            raise ValueError("location_type_custom is required when location_type is 'other'")
        
        if self.location_type != LocationType.other and self.location_type_custom:
            raise ValueError("location_type_custom must be empty unless location_type is 'other'")
        
        return self


class LocationCreate(LocationBase):
    company_id: uuid.UUID
    city_id: uuid.UUID


class LocationUpdate(ORMBaseSchema):
    name: str | None = Field(None, max_length=255)
    location_type: LocationType | None = None
    location_type_custom: str | None = None
    address_line: str | None = Field(None, max_length=510)
    note: str | None = None

    @model_validator(mode="after")
    def validator_location_type(self):
        if self.location_type == LocationType.other and not self.location_type_custom:
            raise ValueError("location_type_custom is required when location_type is 'other'")
    
        if self.location_type is not None and self.location_type != LocationType.other and self.location_type_custom:
            raise ValueError("location_type_custom must be empty unless location_type is 'other'")
    
        return self


class LocationRead(LocationBase, BaseReadSchema):
    company_id: uuid.UUID
    city_id: uuid.UUID