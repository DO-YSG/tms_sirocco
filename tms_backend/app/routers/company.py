import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyRead, CompanyUpdate
from app.dependencies import get_db


router = APIRouter(prefix="/companies", tags=["Companies"])


@router.post("/", response_model=CompanyRead)
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    db_company = Company(**company.model_dump())

    db.add(db_company)
    db.commit()
    db.refresh(db_company)

    return db_company


@router.get("/", response_model=list[CompanyRead])
def get_companies(db: Session = Depends(get_db)):
    companies = db.query(Company).all()
    return companies


@router.get("/{company_id}", response_model=CompanyRead)
def get_company(company_id: uuid.UUID, db: Session = Depends(get_db)):
    company = db.query(Company).filter(Company.id == company_id).first()

    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    return company


@router.put("/{company_id}", response_model=CompanyRead)
def update_company(company_id: uuid.UUID, company_update: CompanyUpdate, db: Session = Depends(get_db)):
    db_company = db.query(Company).filter(Company.id == company_id).first()

    if not db_company:
        raise HTTPException(status_code=404, detail="Company not found")

    update_data = company_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_company, field, value)

    db.commit()
    db.refresh(db_company)

    return db_company


@router.delete("/{company_id}", status_code=204)
def delete_company(company_id: uuid.UUID, db: Session = Depends(get_db)):
    db_company = db.query(Company).filter(Company.id == company_id).first()

    if not db_company:
        raise HTTPException(status_code=404, detail="Company not found")

    db.delete(db_company)
    db.commit()

    return