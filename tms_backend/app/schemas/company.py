import uuid

from pydantic import Field, EmailStr

from app.schemas.base import ORMBaseSchema, BaseReadSchema
from app.models.enums import Status
from app.schemas.country import CountryRead
from app.schemas.city import CityRead


class CompanyBase(ORMBaseSchema):
    name: str = Field(..., max_length=255)
    short_name: str | None = Field(None, max_length=255)
    company_bin: str = Field(..., pattern=r"^\d{12}$")
    country_id: uuid.UUID
    city_id: uuid.UUID
    legal_address: str = Field(..., max_length=510)
    actual_address: str = Field(..., max_length=510)
    phone: str | None = Field(None, max_length=30)
    email: EmailStr | None = None
    website: str | None = Field(None, max_length=255)
    contact_person: str | None = Field(None, max_length=255)
    contact_position: str | None = Field(None, max_length=255)
    company_status: Status = Status.active
    note: str | None = None


class CompanyCreate(CompanyBase):
    pass


class CompanyUpdate(ORMBaseSchema):
    name: str | None = Field(None, max_length=255)
    short_name: str | None = Field(None, max_length=255)
    company_bin: str | None = Field(None, pattern=r"^\d{12}$")
    country_id: uuid.UUID | None = None
    city_id: uuid.UUID | None = None
    legal_address: str | None = Field(None, max_length=510)
    actual_address: str | None = Field(None, max_length=510)
    phone: str | None = Field(None, max_length=30)
    email: EmailStr | None = None
    website: str | None = Field(None, max_length=255)
    contact_person: str | None = Field(None, max_length=255)
    contact_position: str | None = Field(None, max_length=255)
    company_status: Status | None = None
    note: str | None = None


class CompanyRead(CompanyBase, BaseReadSchema):
    pass


class CompanyDetailedRead(CompanyRead):
    country: CountryRead
    city: CityRead