from app.schemas.base import ORMBaseSchema, BaseReadSchema


class CountryBase(ORMBaseSchema):
    name: str
    code: str

class CountryCreate(CountryBase):
    pass

class CountryRead(CountryBase, BaseReadSchema):
    pass