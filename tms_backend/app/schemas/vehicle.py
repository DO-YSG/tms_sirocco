import uuid
from enum import Enum
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class VehicleType(str, Enum):
    truck_tractor = "Седельный тягач"
    semi_trailer = "Полуприцеп"
    tow_truck = "Эвакуатор"
    trailer = "Прицеп"
    car = "Легковой автомобиль"
    van = "Фургон"

class RequiredLicenseCategory(str, Enum):
    a1 = "A1"
    a = "A"
    b1 = "B1"
    b = "B"
    c1 = "C1"
    c = "C"
    d1 = "D1"
    d = "D"
    be = "BE"
    c1e = "C1E"
    ce = "CE"
    d1e = "D1E"
    de = "DE"

class VehicleCategory(str, Enum):
    m1 = "M1"
    m2 = "M2"
    m3 = "M3"
    n1 = "N1"
    n2 = "N2"
    n3 = "N3"
    o1 = "O1"
    o2 = "O2"
    o3 = "O3"

class VehicleBase(BaseModel):
    owner_id: Optional[uuid.UUID] = None
    vehicle_type: VehicleType
    sts_number: str = Field(..., max_length=20)
    plate_number: str = Field(..., max_length=20)
    brand: str = Field(..., max_length=50)
    model: str = Field(..., max_length=50)
    vin: str = Field(..., min_length=17, max_length=17)
    year: int
    required_license_category: RequiredLicenseCategory
    vehicle_category: VehicleCategory
    engine_volume_cc: int
    color: str = Field(..., max_length=30)
    unladen_weight_kg: int
    gross_weight_kg: int
    registered_owner_name: str = Field(..., max_length=100)
    special_notes: Optional[str] = None
    status: bool = True

class VehicleCreate(VehicleBase):
    pass

class VehicleUpdate(BaseModel):
    owner_id: Optional[uuid.UUID] = None
    vehicle_type: Optional[VehicleType] = None
    sts_number: Optional[str] = Field(None, max_length=20)
    plate_number: Optional[str] = Field(None, max_length=20)
    brand: Optional[str] = Field(None, max_length=50)
    model: Optional[str] = Field(None, max_length=50)
    vin: Optional[str] = Field(None, min_length=17, max_length=17)
    year: Optional[int] = None
    required_license_category: Optional[RequiredLicenseCategory] = None
    vehicle_category: Optional[VehicleCategory] = None
    engine_volume_cc: Optional[int] = None
    color: Optional[str] = Field(None, max_length=30)
    unladen_weight_kg: Optional[int] = None
    gross_weight_kg: Optional[int] = None
    registered_owner_name: Optional[str] = Field(None, max_length=100)
    special_notes: Optional[str] = None
    status: Optional[bool] = None

class VehicleRead(VehicleBase):
    id: uuid.UUID
    created_by: Optional[str] = None
    updated_by: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True