import uuid
from typing import Optional

from pydantic import Field, EmailStr

from app.schemas.base import ORMBaseSchema, BaseReadSchema
from app.models.company import CompanyStatus
from app.schemas.country import CountryRead
from app.schemas.city import CityRead


class CompanyBase(ORMBaseSchema):
    name: str = Field(..., max_length=255)
    short_name: Optional[str] = Field(None, max_length=255)
    company_bin: str = Field(..., min_length=12, max_length=12)
    country_id: uuid.UUID
    city_id: uuid.UUID
    legal_address: str = Field(..., max_length=510)
    actual_address: str = Field(..., max_length=510)
    phone: Optional[str] = Field(None, max_length=30)
    email: Optional[EmailStr] = None
    website: Optional[str] = Field(None, max_length=255)
    contact_person: Optional[str] = Field(None, max_length=255)
    contact_position: Optional[str] = Field(None, max_length=255)
    company_status: CompanyStatus = CompanyStatus.active
    note: Optional[str] = None


class CompanyCreate(CompanyBase):
    pass


class CompanyUpdate(ORMBaseSchema):
    name: Optional[str] = Field(None, max_length=255)
    short_name: Optional[str] = Field(None, max_length=255)
    company_bin: Optional[str] = Field(None, min_length=12, max_length=12)
    country_id: Optional[uuid.UUID] = None
    city_id: Optional[uuid.UUID] = None
    legal_address: Optional[str] = Field(None, max_length=510)
    actual_address: Optional[str] = Field(None, max_length=510)
    phone: Optional[str] = Field(None, max_length=30)
    email: Optional[EmailStr] = None
    website: Optional[str] = Field(None, max_length=255)
    contact_person: Optional[str] = Field(None, max_length=255)
    contact_position: Optional[str] = Field(None, max_length=255)
    company_status: Optional[CompanyStatus] = None
    note: Optional[str] = None


class CompanyRead(CompanyBase, BaseReadSchema):
    country: CountryRead
    city: CityRead