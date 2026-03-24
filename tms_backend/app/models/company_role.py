import enum

from app.core.database import Base
from app.models.base import BaseModelMixin

from sqlalchemy import Column, Text, Enum, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class CompanyRoleList(str, enum.Enum):
    customer = "customer"
    payer = "payer"
    carrier = "carrier"
    partner = "partner"
    supplier = "supplier"


class CompanyRole(Base, BaseModelMixin):
    __tablename__ = "company_roles"

    company_id = Column(UUID(as_uuid=True), ForeignKey("companies.id"), nullable=False, index=True)
    role = Column(Enum(CompanyRoleList, name="company_role_list_enum"), nullable=False, index=True)
    note = Column(Text, nullable=True)

    __table_args__ = (
        UniqueConstraint("company_id", "role", name="uq_company_role"),
    )

    company = relationship("Company", back_populates="roles")