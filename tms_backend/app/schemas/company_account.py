import uuid

from pydantic import Field

from app.schemas.base import ORMBaseSchema, BaseReadSchema
from app.models.enums import Currency

class CompanyAccountBase(ORMBaseSchema):
    bank_name: str = Field(..., max_length=255)
    bank_bik: str = Field(..., max_length=20)
    bank_account: str = Field(..., max_length=50)
    currency: Currency
    is_default: bool = False
    swift: str | None = Field(None, max_length=20)
    note: str | None = None


class CompanyAccountCreate(CompanyAccountBase):
    pass


class CompanyAccountUpdate(ORMBaseSchema):
    bank_name: str | None = Field(None, max_length=255)
    bank_bik: str | None = Field(None, max_length=20)
    is_default: bool | None = None
    swift: str | None = Field(None, max_length=20)
    note: str | None = None


class CompanyAccountRead(CompanyAccountBase, BaseReadSchema):
    company_id: uuid.UUID