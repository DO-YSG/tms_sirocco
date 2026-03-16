import uuid
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from app.models.company import CompanyType, Currency


class CompanyBase(BaseModel):
    name: str
    short_name: Optional[str] = None
    company_type: CompanyType
    status: Optional[bool] = True

    bin: Optional[str] = None
    registration_number: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    legal_address: Optional[str] = None
    actual_address: Optional[str] = None
    postal_code: Optional[str] = None

    company_role: Optional[str] = None
    transport_types: Optional[str] = None
    owns_vehicles: Optional[bool] = None
    fleet_size: Optional[int] = None

    phone: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    contact_person: Optional[str] = None
    contact_position: Optional[str] = None

    bank_name: Optional[str] = None
    bank_account: Optional[str] = None
    swift: Optional[str] = None
    currency: Optional[Currency] = None
    payment_terms: Optional[str] = None

    note: Optional[str] = None
    tariff_plan: Optional[str] = "basic"


class CompanyCreate(CompanyBase):
    pass


class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    short_name: Optional[str] = None
    company_type: Optional[CompanyType] = None
    status: Optional[bool] = None

    bin: Optional[str] = None
    registration_number: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    legal_address: Optional[str] = None
    actual_address: Optional[str] = None
    postal_code: Optional[str] = None

    company_role: Optional[str] = None
    transport_types: Optional[str] = None
    owns_vehicles: Optional[bool] = None
    fleet_size: Optional[int] = None

    phone: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    contact_person: Optional[str] = None
    contact_position: Optional[str] = None

    bank_name: Optional[str] = None
    bank_account: Optional[str] = None
    swift: Optional[str] = None
    currency: Optional[Currency] = None
    payment_terms: Optional[str] = None

    note: Optional[str] = None
    tariff_plan: Optional[str] = None


class CompanyRead(CompanyBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    created_by: Optional[str] = None
    updated_by: Optional[str] = None

    class Config:
        from_attributes = True