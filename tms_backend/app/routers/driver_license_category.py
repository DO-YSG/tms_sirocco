from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.driver_license_category import DriverLicenseCategoryCreate, DriverLicenseCategoryRead, DriverLicenseCategoryUpdate
from app.services.driver_license_category import DriverLicenseCategoryService


router = APIRouter(prefix="/driver-license-categories", tags=["Driver License Categories"])


@router.post("/", response_model=DriverLicenseCategoryRead)
def create_driver_license_category(
    data: DriverLicenseCategoryCreate,
    db: Session = Depends(get_db),
):
    service = DriverLicenseCategoryService(db)
    return service.create(data)


@router.get("/{category_id}", response_model=DriverLicenseCategoryRead)
def get_driver_license_category(
    category_id: UUID,
    db: Session = Depends(get_db),
):
    service = DriverLicenseCategoryService(db)
    return service.get_by_id(category_id)


@router.get("/driver/{driver_id}", response_model=list[DriverLicenseCategoryRead])
def get_driver_license_categories_by_driver(
    driver_id: UUID,
    db: Session = Depends(get_db),
):
    service = DriverLicenseCategoryService(db)
    return service.get_by_driver_id(driver_id)


@router.patch("/{category_id}", response_model=DriverLicenseCategoryRead)
def update_driver_license_category(
    category_id: UUID,
    data: DriverLicenseCategoryUpdate,
    db: Session = Depends(get_db),
):
    service = DriverLicenseCategoryService(db)
    return service.update(category_id, data)


@router.delete("/{category_id}")
def delete_driver_license_category(
    category_id: UUID,
    db: Session = Depends(get_db),
):
    service = DriverLicenseCategoryService(db)
    service.delete(category_id)
    return {"detail": "Driver license category deleted successfully"}