from uuid import UUID

from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.driver_license_category import DriverLicenseCategory
from app.schemas.driver_license_category import DriverLicenseCategoryCreate, DriverLicenseCategoryUpdate
from app.repositories.driver_license_category import DriverLicenseCategoryRepository


class DriverLicenseCategoryService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = DriverLicenseCategoryRepository(db)

    def create(self, data: DriverLicenseCategoryCreate) -> DriverLicenseCategory:
        exists = self.repository.exists(driver_id=data.driver_id, category=data.category)
        if exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Driver already has this license category",
            )

        obj = DriverLicenseCategory(driver_id=data.driver_id, category=data.category)

        try:
            self.repository.create(obj)
            self.db.commit()
            self.db.refresh(obj)
            return obj
        except Exception:
            self.db.rollback()
            raise

    def get_by_id(self, category_id: UUID) -> DriverLicenseCategory:
        obj = self.repository.get_by_id(category_id)
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Driver license category not found",
            )
        return obj

    def get_by_driver_id(self, driver_id: UUID) -> list[DriverLicenseCategory]:
        return self.repository.get_by_driver_id(driver_id)

    def update(self, category_id: UUID, data: DriverLicenseCategoryUpdate) -> DriverLicenseCategory:
        obj = self.repository.get_by_id(category_id)
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Driver license category not found",
            )

        update_data = data.model_dump(exclude_unset=True)

        if "category" in update_data:
            duplicate_exists = self.repository.exists(
                driver_id=obj.driver_id,
                category=update_data["category"],
            )
            if duplicate_exists and update_data["category"] != obj.category:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Driver already has this license category",
                )

            obj.category = update_data["category"]

        try:
            self.db.commit()
            self.db.refresh(obj)
            return obj
        except Exception:
            self.db.rollback()
            raise

    def delete(self, category_id: UUID) -> None:
        obj = self.repository.get_by_id(category_id)
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Driver license category not found",
            )

        try:
            self.repository.delete(obj)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise