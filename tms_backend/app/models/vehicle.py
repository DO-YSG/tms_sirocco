from sqlalchemy import Column, String, Text, Integer, ForeignKey, CheckConstraint, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base
from app.models.base import BaseModelMixin
from app.models.enums import StatusType, LicenseCategoryType, VehicleTypeType, VehicleCategoryType


class Vehicle(Base, BaseModelMixin):
    __tablename__ = "vehicles"

    owner_id = Column(UUID(as_uuid=True), ForeignKey("companies.id", ondelete="SET NULL"), nullable=True, index=True)
    
    vehicle_type = Column(VehicleTypeType, nullable=False, index=True)
    plate_number = Column(String(20), unique=True, nullable=False, index=True)
    sts_number = Column(String(20), unique=True, nullable=False, index=True)
    brand = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    vin = Column(String(17), unique=True, nullable=False, index=True)
    year = Column(Integer, nullable=False)
    required_license_category = Column(LicenseCategoryType, nullable=False)
    vehicle_category = Column(VehicleCategoryType, nullable=False)
    engine_volume_cc = Column(Integer, nullable=True)
    color = Column(String(50), nullable=False)
    unladen_weight_kg = Column(Integer, nullable=False)
    gross_weight_kg = Column(Integer, nullable=False)
    registered_owner_name = Column(String(255), nullable=False)
    special_notes = Column(Text, nullable=True)

    status = Column(StatusType, server_default=text("'active'::status"), nullable=False)

    owner = relationship("Company", back_populates="vehicles", passive_deletes=True)

    __table_args__ = (
        CheckConstraint("length(plate_number) >= 5", name="ck_vehicle_plate_length"),
        CheckConstraint("year >= 1900", name="ck_vehicle_year_min"),
        CheckConstraint("unladen_weight_kg > 0", name="ck_vehicle_unladen_weight_positive"),
        CheckConstraint("gross_weight_kg > 0", name="ck_vehicle_gross_weight_positive"),
        CheckConstraint("gross_weight_kg >= unladen_weight_kg", name="ck_vehicle_weight_valid"),
        CheckConstraint("engine_volume_cc IS NULL OR engine_volume_cc > 0", name="ck_vehicle_engine_volume_positive"),
        CheckConstraint("length(vin) = 17", name="ck_vehicle_vin_length"),
    )