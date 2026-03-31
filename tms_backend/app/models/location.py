import enum

from sqlalchemy import Column, String, Text, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base
from app.models.base import BaseModelMixin
from app.models.enums import LocationTypeType


class Location(Base, BaseModelMixin):
    __tablename__ = "locations"

    company_id = Column(UUID(as_uuid=True), ForeignKey("companies.id"), nullable=False, index=True)
    city_id = Column(UUID(as_uuid=True), ForeignKey("cities.id"), nullable=False, index=True)

    name = Column(String(255), nullable=False, index=True)
    location_type = Column(LocationTypeType, nullable=False)
    location_type_custom = Column(Text, nullable=True)
    address_line = Column(String(510), nullable=True)
    note = Column(Text, nullable=True)

    company = relationship("Company", back_populates="locations")
    city = relationship("City", back_populates="locations")

    __table_args__ = (
        UniqueConstraint("company_id", "name", "city_id", name="uq_company_location_name_city"),
    )