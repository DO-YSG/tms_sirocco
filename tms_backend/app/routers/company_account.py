import uuid

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.services.company_account import CompanyAccountService
from app.schemas.company_account import CompanyAccountCreate, CompanyAccountUpdate, CompanyAccountRead

router = APIRouter(prefix="/companies/{company_id}/accounts", tags=["company accounts"])


@router.get("/", response_model=list[CompanyAccountRead])
def get_company_accounts(company_id: uuid.UUID, db: Session = Depends(get_db)):
    service = CompanyAccountService(db)
    return service.get_by_company(company_id)


@router.get("/{account_id}", response_model=CompanyAccountRead)
def get_company_account(company_id: uuid.UUID, account_id: uuid.UUID, db: Session = Depends(get_db)):
    service = CompanyAccountService(db)
    return service.get_by_id(company_id, account_id)


@router.post("/", response_model=CompanyAccountRead, status_code=status.HTTP_201_CREATED)
def create_company_account(company_id: uuid.UUID, data: CompanyAccountCreate, db: Session = Depends(get_db)):
    service = CompanyAccountService(db)
    return service.create(company_id, data)


@router.patch("/{account_id}", response_model=CompanyAccountRead)
def update_company_account(company_id: uuid.UUID, account_id: uuid.UUID, data: CompanyAccountUpdate, db: Session = Depends(get_db)):
    service = CompanyAccountService(db)
    return service.update(company_id, account_id, data)


@router.delete("/{account_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_company_account(company_id: uuid.UUID, account_id: uuid.UUID, db: Session = Depends(get_db)):
    service = CompanyAccountService(db)
    service.delete(company_id, account_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)