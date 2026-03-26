import uuid

from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyUpdate


class CompanyRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> Sequence[Company]:
        stmt = select(Company).order_by(Company.name)
        return self.db.execute(stmt).scalars().all()

    def get_all_detailed(self) -> Sequence[Company]:
        stmt = select(Company).options(joinedload(Company.country), joinedload(Company.city)).order_by(Company.name)
        return self.db.execute(stmt).scalars().all()

    def get_by_id(self, company_id: uuid.UUID) -> Company | None:
        stmt = select(Company).where(Company.id == company_id)
        return self.db.execute(stmt).scalar_one_or_none()

    def get_by_id_detailed(self, company_id: uuid.UUID) -> Company | None:
        stmt = select(Company).options(joinedload(Company.country), joinedload(Company.city)).where(Company.id == company_id)
        return self.db.execute(stmt).scalar_one_or_none()

    def get_by_bin(self, company_bin: str) -> Company | None:
        stmt = select(Company).where(Company.company_bin == company_bin)
        return self.db.execute(stmt).scalar_one_or_none()

    def exists_by_id(self, company_id: uuid.UUID) -> bool:
        stmt = select(Company.id).where(Company.id == company_id)
        return self.db.execute(stmt).first() is not None

    def exists_by_bin(self, company_bin: str) -> bool:
        stmt = select(Company.id).where(Company.company_bin == company_bin)
        return self.db.execute(stmt).first() is not None

    def create(self, data: CompanyCreate) -> Company:
        company = Company(**data.model_dump())
        self.db.add(company)
        return company

    def update(self, company: Company, data: CompanyUpdate) -> Company:
        update_data = data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(company, field, value)

        return company