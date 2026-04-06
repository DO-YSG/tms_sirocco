from uuid import UUID

from sqlalchemy.orm import Session

from app.models.driver_license_category import DriverLicenseCategory


class DriverLicenseCategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, obj: DriverLicenseCategory) -> DriverLicenseCategory:
        self.db.add(obj)
        return obj

    def get_by_id(self, id: UUID) -> DriverLicenseCategory | None:
        return self.db.query(DriverLicenseCategory).filter(DriverLicenseCategory.id == id).first()

    def get_by_driver_id(self, driver_id: UUID) -> list[DriverLicenseCategory]:
        return self.db.query(DriverLicenseCategory).filter(
            DriverLicenseCategory.driver_id == driver_id
        ).all()

    def exists(self, driver_id: UUID, category) -> bool:
        return self.db.query(DriverLicenseCategory).filter(
            DriverLicenseCategory.driver_id == driver_id,
            DriverLicenseCategory.category == category
        ).first() is not None

    def delete(self, obj: DriverLicenseCategory) -> None:
        self.db.delete(obj)