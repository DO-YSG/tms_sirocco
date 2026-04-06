from sqlalchemy import Column, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.models.base import BaseModelMixin
from app.models.enums import LicenseCategoryType


class DriverLicenseCategory(Base, BaseModelMixin):
    __tablename__ = "driver_license_categories"

    driver_id = Column(UUID(as_uuid=True), ForeignKey("drivers.id"), nullable=False, index=True)
    category = Column(LicenseCategoryType, nullable=False, index=True)

    driver = relationship("Driver", back_populates="license_categories")

    __table_args__ = (
        UniqueConstraint("driver_id", "category", name="uq_driver_license_category"),
    )