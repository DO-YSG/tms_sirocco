import uuid

from pydantic import Field, field_validator

from app.schemas.base import ORMBaseSchema, BaseReadSchema


class CityDistanceBase(ORMBaseSchema):
    city1_id: uuid.UUID
    city2_id: uuid.UUID
    distance_km: int = Field(..., gt=0)

    @field_validator("city2_id")
    @classmethod
    def validate_cities_not_equal(cls, v, info):
        if "city1_id" in info.data and v == info.data["city1_id"]:
            raise ValueError("city1_id and city2_id must be different")
        return v


class CityDistanceCreate(CityDistanceBase):
    pass


class CityDistanceUpdate(ORMBaseSchema):
    city1_id: uuid.UUID | None = None
    city2_id: uuid.UUID | None = None
    distance_km: int | None = Field(None, gt=0)

    @field_validator("city2_id")
    @classmethod
    def validate_cities_not_equal(cls, v, info):
        if v is not None and "city1_id" in info.data and info.data["city1_id"] is not None and v == info.data["city1_id"]:
            raise ValueError("city1_id and city2_id must be different")
        return v


class CityDistanceRead(CityDistanceBase, BaseReadSchema):
    pass