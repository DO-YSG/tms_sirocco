import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.services.company import CompanyService
from app.schemas.company import (
    CompanyCreate,
    CompanyUpdate,
    CompanyRead,
)

router = APIRouter(prefix="/companies", tags=["Companies"])


@router.get("/", response_model=list[CompanyRead])
def get_companies(db: Session = Depends(get_db)):
    service = CompanyService(db)
    return service.get_all_companies()


@router.get("/{company_id}", response_model=CompanyRead)
def get_company(company_id: uuid.UUID, db: Session = Depends(get_db)):
    service = CompanyService(db)
    company = service.get_company_by_id(company_id)

    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found",
        )

    return company


@router.post("/", response_model=CompanyRead, status_code=status.HTTP_201_CREATED)
def create_company(company_in: CompanyCreate, db: Session = Depends(get_db)):
    service = CompanyService(db)

    # бизнес-проверка
    if service.company_exists_by_bin(company_in.company_bin):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Company with this BIN already exists",
        )

    return service.create_company(company_in)


@router.put("/{company_id}", response_model=CompanyRead)
def update_company(
    company_id: uuid.UUID,
    company_in: CompanyUpdate,
    db: Session = Depends(get_db),
):
    service = CompanyService(db)

    company = service.update_company(company_id, company_in)

    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found",
        )

    return company


@router.delete("/{company_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_company(company_id: uuid.UUID, db: Session = Depends(get_db)):
    service = CompanyService(db)

    deleted = service.delete_company(company_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found",
        )