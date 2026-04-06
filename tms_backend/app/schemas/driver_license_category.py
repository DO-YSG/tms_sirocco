import uuid

from app.schemas.base import ORMBaseSchema, BaseReadSchema
from app.models.enums import LicenseCategory


class DriverLicenseCategoryBase(ORMBaseSchema):
    category: LicenseCategory


class DriverLicenseCategoryCreate(DriverLicenseCategoryBase):
    driver_id: uuid.UUID


class DriverLicenseCategoryUpdate(ORMBaseSchema):
    category: LicenseCategory | None = None


class DriverLicenseCategoryRead(DriverLicenseCategoryBase, BaseReadSchema):
    driver_id: uuid.UUID