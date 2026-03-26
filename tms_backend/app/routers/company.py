import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.services.company import CompanyService, CompanyNotFoundError, CompanyAlreadyExistsError

from app.schemas.company import CompanyCreate, CompanyUpdate, CompanyRead

router = APIRouter(prefix="/companies", tags=["companies"])


@router.get("/", response_model=list[CompanyRead])
def get_companies(db: Session = Depends(get_db)):
    service = CompanyService(db)
    return service.get_all_companies()


@router.get("/{company_id}", response_model=CompanyRead)
def get_company(company_id: uuid.UUID, db: Session = Depends(get_db)):
    service = CompanyService(db)
    try:
        return service.get_company_by_id(company_id)
    except CompanyNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=CompanyRead, status_code=status.HTTP_201_CREATED)
def create_company(company_in: CompanyCreate, db: Session = Depends(get_db)):
    service = CompanyService(db)
    try:
        return service.create_company(company_in)
    except CompanyAlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{company_id}", response_model=CompanyRead)
def update_company(
    company_id: uuid.UUID,
    company_in: CompanyUpdate,
    db: Session = Depends(get_db),
):
    service = CompanyService(db)
    try:
        return service.update_company(company_id, company_in)
    except CompanyNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except CompanyAlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e))