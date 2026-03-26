from app.core.database import Base
from app.models.base import BaseModelMixin
from app.models.enums import CompanyStatusType, CompanyStatus

from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID


class Company(Base, BaseModelMixin):
    __tablename__ = "companies"

    name = Column(String(255), nullable=False, index=True)
    short_name = Column(String(255), nullable=True)
    company_bin = Column(String(12), unique=True, nullable=False) # Business Identification Number (KZ)
    country_id = Column(UUID(as_uuid=True), ForeignKey("countries.id"), nullable=False, index=True)
    city_id = Column(UUID(as_uuid=True), ForeignKey("cities.id"), nullable=False, index=True)
    legal_address = Column(String(510), nullable=False)
    actual_address = Column(String(510), nullable=False)
    phone = Column(String(30), nullable=True)
    email = Column(String(255), nullable=True)
    website = Column(String(255), nullable=True)
    contact_person = Column(String(255), nullable=True)
    contact_position = Column(String(255), nullable=True)
    company_status = Column(CompanyStatusType, nullable=False, default=CompanyStatus.ACTIVE, index=True)
    note = Column(Text, nullable=True)

    country = relationship("Country", back_populates="companies")
    city = relationship("City", back_populates="companies")
    roles = relationship("CompanyRole", back_populates="company", cascade="all, delete-orphan")
    accounts = relationship("CompanyAccount", back_populates="company", cascade="all, delete-orphan")