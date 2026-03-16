import enum

from app.core.database import Base
from app.models.base import BaseModelMixin

from sqlalchemy import Column, String, Text, ForeignKey, UniqueConstraint, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class LocationType(enum.Enum):
    plant = "plant"
    warehouse = "warehouse"
    dealer = "dealer"
    parking = "parking"
    service = "service"
    other = "other"


class Location(Base, BaseModelMixin):
    __tablename__ = "locations"

    company_id = Column(UUID(as_uuid=True), ForeignKey("companies.id"), nullable=False, index=True)
    city_id = Column(UUID(as_uuid=True), ForeignKey("cities.id"), nullable=False, index=True)

    name = Column(String(255), nullable=False)
    location_type = Column(Enum(LocationType, name = "location_type_enum"), nullable=False)
    location_type_custom = Column(Text, nullable=True)

    address_line = Column(String(255), nullable=True)
    
    note = Column(Text, nullable=True)

    __table_args__ = (
        UniqueConstraint("name", "city_id", name="uq_location_name_city"),
    )