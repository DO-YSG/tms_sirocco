import uuid
from typing import Sequence

from sqlalchemy.orm import Session

from app.models.company import Company
from app.models.enums import CompanyStatus
from app.schemas.company import CompanyCreate, CompanyUpdate
from app.repositories.company import CompanyRepository


class CompanyNotFoundError(Exception):
    pass


class CompanyAlreadyExistsError(Exception):
    pass


class CompanyService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = CompanyRepository(db)

    def get_all_companies(self) -> Sequence[Company]:
        return self.repository.get_all()

    def get_all_companies_detailed(self) -> Sequence[Company]:
        return self.repository.get_all_detailed()

    def get_company_by_id(self, company_id: uuid.UUID) -> Company:
        company = self.repository.get_by_id(company_id)
        if not company:
            raise CompanyNotFoundError("Company not found")
        return company

    def get_company_by_id_detailed(self, company_id: uuid.UUID) -> Company:
        company = self.repository.get_by_id_detailed(company_id)
        if not company:
            raise CompanyNotFoundError("Company not found")
        return company

    def create_company(self, data: CompanyCreate) -> Company:
        if self.repository.exists_by_bin(data.company_bin):
            raise CompanyAlreadyExistsError("Company with this BIN already exists")

        try:
            company = self.repository.create(data)
            self.db.commit()
            self.db.refresh(company)
            return company
        except Exception:
            self.db.rollback()
            raise

    def update_company(self, company_id: uuid.UUID, data: CompanyUpdate) -> Company:
        company = self.repository.get_by_id(company_id)
        if not company:
            raise CompanyNotFoundError("Company not found")

        if data.company_bin is not None and data.company_bin != company.company_bin:
            if self.repository.exists_by_bin(data.company_bin):
                raise CompanyAlreadyExistsError("Company with this BIN already exists")

        try:
            company = self.repository.update(company, data)
            self.db.commit()
            self.db.refresh(company)
            return company
        except Exception:
            self.db.rollback()
            raise

    def archive_company(self, company_id: uuid.UUID) -> Company:
        company = self.repository.get_by_id(company_id)
        if not company:
            raise CompanyNotFoundError("Company not found")

        try:
            company.company_status = CompanyStatus.ARCHIVED
            self.db.commit()
            self.db.refresh(company)
            return company
        except Exception:
            self.db.rollback()
            raise