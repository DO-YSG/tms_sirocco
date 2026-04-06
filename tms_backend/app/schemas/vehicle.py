import uuid

from pydantic import Field

from app.models.enums import VehicleType, LicenseCategory, VehicleCategory, Status
from app.schemas.base import ORMBaseSchema, BaseReadSchema


class VehicleBase(ORMBaseSchema):
    owner_id: uuid.UUID | None = None
    vehicle_type: VehicleType
    plate_number: str = Field(..., min_length=5, max_length=20)
    sts_number: str = Field(..., max_length=20)
    brand: str = Field(..., max_length=50)
    model: str = Field(..., max_length=50)
    vin: str = Field(..., min_length=17, max_length=17)
    year: int = Field(..., ge=1900)
    required_license_category: LicenseCategory
    vehicle_category: VehicleCategory
    engine_volume_cc: int | None = None
    color: str = Field(..., max_length=50)
    unladen_weight_kg: int = Field(..., gt=0)
    gross_weight_kg: int = Field(..., gt=0)
    registered_owner_name: str = Field(..., max_length=255)
    special_notes: str | None = None


class VehicleCreate(VehicleBase):
    pass


class VehicleUpdate(ORMBaseSchema):
    owner_id: uuid.UUID | None = None
    vehicle_type: VehicleType | None = None
    plate_number: str | None = Field(None, min_length=5, max_length=20)
    sts_number: str | None = Field(None, max_length=20)
    brand: str | None = Field(None, max_length=50)
    model: str | None = Field(None, max_length=50)
    vin: str | None = Field(None, min_length=17, max_length=17)
    year: int | None = Field(None, ge=1900)
    required_license_category: LicenseCategory | None = None
    vehicle_category: VehicleCategory | None = None
    engine_volume_cc: int | None = None
    color: str | None = Field(None, max_length=50)
    unladen_weight_kg: int | None = Field(None, gt=0)
    gross_weight_kg: int | None = Field(None, gt=0)
    registered_owner_name: str | None = Field(None, max_length=255)
    special_notes: str | None = None
    status: Status | None = None


class VehicleRead(VehicleBase , BaseReadSchema):
    status: Status