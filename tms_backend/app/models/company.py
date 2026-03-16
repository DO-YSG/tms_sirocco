import enum

from app.core.database import Base
from app.models.base import BaseModelMixin

from sqlalchemy import Column, String, Text, Enum
from sqlalchemy.orm import relationship


class CompanyStatus(str, enum.Enum):
    active = "active"
    inactive = "inactive"
    blocked = "blocked"
    archived = "archived"


class Company(Base, BaseModelMixin):
    __tablename__ = "companies"

    name = Column(String(255), nullable=False, index=True)
    short_name = Column(String(255), nullable=True)
    bin = Column(String(12), unique=True, nullable=False)
    
    legal_address = Column(String(255), nullable=False)
    actual_address = Column(String(255), nullable=False)

    phone = Column(String(30), nullable=True)
    email = Column(String(255), unique=False, nullable=True)
    website = Column(String(255), nullable=True)
    
    contact_person = Column(String(255), nullable=True)
    contact_position = Column(String(255), nullable=True)

    note = Column(Text, nullable=True)

    company_status = Column(Enum(CompanyStatus, name="company_status_enum"), nullable=False, default=CompanyStatus.active, index=True)

    roles = relationship("CompanyRole", back_populates="company")
    accounts = relationship("CompanyAccount", back_populates="company")