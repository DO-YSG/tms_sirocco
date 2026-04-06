from sqlalchemy import Column, String, Date, Text, ForeignKey, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models.base import BaseModelMixin
from app.models.enums import StatusType, Status


class Driver(Base, BaseModelMixin):
    __tablename__ = "drivers"

    company_id = Column(UUID(as_uuid=True), ForeignKey("companies.id"), nullable=False, index=True)
    last_name = Column(String(255), nullable=False)
    first_name = Column(String(255), nullable=False)
    middle_name = Column(String(255), nullable=True)

    driving_license_number = Column(String(225), unique=True, nullable=False, index=True)
    date_of_birth = Column(Date, nullable=False)
    date_of_issue = Column(Date, nullable=False)
    expiration_date = Column(Date, nullable=False)

    status = Column(StatusType, default=Status.active, nullable=False)
    note = Column(Text, nullable=True)

    license_categories = relationship("DriverLicenseCategory", back_populates="driver", cascade="all, delete-orphan")
    company = relationship("Company", back_populates="drivers")

    __table_args__ = (
        CheckConstraint("expiration_date > date_of_issue", name="ck_expiration_date_date_of_issue"),
        CheckConstraint("date_of_issue > date_of_birth", name="ck_date_of_issue_date_of_birth"),
    )