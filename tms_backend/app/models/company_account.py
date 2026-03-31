from sqlalchemy import Column, String, Text, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base
from app.models.base import BaseModelMixin
from app.models.enums import CurrencyType


class CompanyAccount(Base, BaseModelMixin):
    __tablename__ = "company_accounts"

    company_id = Column(UUID(as_uuid=True), ForeignKey("companies.id"), nullable=False, index=True)

    bank_name = Column(String(255), nullable=False)
    bank_bik = Column(String(20), nullable=False)
    bank_account = Column(String(50), nullable=False)
    currency = Column(CurrencyType, nullable=False)
    is_default = Column(Boolean, default=False, nullable=False)
    swift = Column(String(20), nullable=True)
    note = Column(Text, nullable=True)

    company = relationship("Company", back_populates="accounts")

    __table_args__ = (
        UniqueConstraint("company_id", "bank_account", "currency", name="uq_company_account"),
    )