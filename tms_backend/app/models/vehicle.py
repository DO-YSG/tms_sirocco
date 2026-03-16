import enum

from app.core.database import Base
from app.models.base import BaseModelMixin

from sqlalchemy import Column, String, Text, Integer, Enum, ForeignKey, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID


class VehicleType(str, enum.Enum):
    truck_tractor = "truck_tractor"
    semi_trailer = "semi_trailer"
    tow_truck = "tow_truck"
    trailer = "trailer"
    car = "car"
    van = "van"

class RequiredLicenseCategory(str, enum.Enum):
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

class VehicleCategory(str, enum.Enum):
    m1 = "M1"
    m2 = "M2"
    m3 = "M3"
    n1 = "N1"
    n2 = "N2"
    n3 = "N3"
    o1 = "O1"
    o2 = "O2"
    o3 = "O3"

class VehicleStatus (str, enum.Enum):
    active = "active"
    inactive = "inactive"

class Vehicle(Base, BaseModelMixin):
    __tablename__ = "vehicles"

    owner_id = Column(UUID(as_uuid=True), ForeignKey("companies.id"), index=True, nullable=True)
    
    vehicle_type = Column(Enum(VehicleType, name="vehicle_type_enum"), nullable=False)
    plate_number = Column(String(20), unique=True, nullable=False)
    sts_number = Column(String(20), unique=True, nullable=False)
    brand = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    vin = Column(String(17), unique=True, nullable=False)
    year = Column(Integer, nullable=False)
    required_license_category = Column(Enum(RequiredLicenseCategory, name="required_license_category_enum"), nullable=False)
    vehicle_category = Column(Enum(VehicleCategory, name="vehicle_category_enum"), nullable=False)
    engine_volume_cc = Column(Integer, nullable=True)
    color = Column(String(50), nullable=False)
    unladen_weight_kg = Column(Integer, nullable=False)
    gross_weight_kg = Column(Integer, nullable=False)
    registered_owner_name = Column(String(255), nullable=False)
    special_notes = Column(Text, nullable=True)

    status = Column(Enum(VehicleStatus, name="vehicle_status_enum"), default=VehicleStatus.active, nullable=False)

    __table_args__ = (
        CheckConstraint("year > 1900", name="ck_vehicle_year_positive"),
        CheckConstraint("unladen_weight_kg > 0", name="ck_vehicle_unladen_weight_positive"),
        CheckConstraint("gross_weight_kg > 0", name="ck_vehicle_gross_weight_positive"),
    )