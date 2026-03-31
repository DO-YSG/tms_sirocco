from pydantic import Field

from app.schemas.base import ORMBaseSchema, BaseReadSchema


class CountryBase(ORMBaseSchema):
    name: str = Field(..., max_length=255)
    code: str = Field(..., min_length=3, max_length=3)


class CountryCreate(CountryBase):
    pass


class CountryRead(CountryBase, BaseReadSchema):
    pass