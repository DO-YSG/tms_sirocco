import uuid
from typing import Optional
from pydantic import Field

from app.schemas.base import ORMBaseSchema, BaseReadSchema
from app.models.enums import Currency

class CompanyAccountBase(ORMBaseSchema):
    bank_name: str = Field(..., max_length=255)
    bank_bik: str = Field(..., max_length=20)
    bank_account: str = Field(..., max_length=50)
    currency: Currency
    is_default: bool = False
    swift: Optional[str] = Field(None, max_length=20)
    note: Optional[str] = None


class CompanyAccountCreate(CompanyAccountBase):
    pass


class CompanyAccountUpdate(ORMBaseSchema):
    bank_name: Optional[str] = Field(None, max_length=255)
    bank_bik: Optional[str] = Field(None, max_length=20)
    is_default: Optional[bool] = None
    swift: Optional[str] = Field(None, max_length=20)
    note: Optional[str] = None


class CompanyAccountRead(CompanyAccountBase, BaseReadSchema):
    company_id: uuid.UUID