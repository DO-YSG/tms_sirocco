import uuid

from pydantic import Field

from app.schemas.base import ORMBaseSchema, BaseReadSchema
from app.schemas.country import CountryRead


class CityBase(ORMBaseSchema):
    name: str = Field(..., max_length=255)
    region: str = Field(..., max_length=255)
    country_id: uuid.UUID


class CityCreate(CityBase):
    pass


class CityUpdate(ORMBaseSchema):
    name: str | None = Field(None, max_length=255)
    region: str | None = Field(None, max_length=255)
    country_id: uuid.UUID | None = None


class CityRead(CityBase, BaseReadSchema):
    country: CountryRead