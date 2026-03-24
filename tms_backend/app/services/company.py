import uuid

from sqlalchemy.orm import Session

from app.models import Company
from app.repositories.company import CompanyRepository
from app.schemas.company import CompanyCreate, CompanyUpdate


class CompanyService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = CompanyRepository(db)

    def get_all_companies(self) -> list[Company]:
        return self.repository.get_all()

    def get_company_by_id(self, company_id: uuid.UUID) -> Company | None:
        return self.repository.get_by_id(company_id)

    def get_company_by_bin(self, company_bin: str) -> Company | None:
        return self.repository.get_by_company_bin(company_bin)

    def create_company(self, company_in: CompanyCreate) -> Company:
        company = Company(
            name=company_in.name,
            short_name=company_in.short_name,
            company_bin=company_in.company_bin,
            country_id=company_in.country_id,
            city_id=company_in.city_id,
            legal_address=company_in.legal_address,
            actual_address=company_in.actual_address,
            phone=company_in.phone,
            email=company_in.email,
            website=company_in.website,
            contact_person=company_in.contact_person,
            contact_position=company_in.contact_position,
            company_status=company_in.company_status,
            note=company_in.note,
        )

        try:
            self.repository.create(company)
            self.db.commit()
            self.db.refresh(company)
            return company
        except Exception:
            self.db.rollback()
            raise

    def update_company(self, company_id: uuid.UUID, company_in: CompanyUpdate) -> Company | None:
        company = self.repository.get_by_id(company_id)
        if not company:
            return None

        update_data = company_in.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(company, field, value)

        try:
            self.repository.update(company)
            self.db.commit()
            self.db.refresh(company)
            return company
        except Exception:
            self.db.rollback()
            raise

    def delete_company(self, company_id: uuid.UUID) -> bool:
        company = self.repository.get_by_id(company_id)
        if not company:
            return False

        try:
            self.repository.delete(company)
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            raise

    def company_exists_by_id(self, company_id: uuid.UUID) -> bool:
        return self.repository.exists_by_id(company_id)

    def company_exists_by_bin(self, company_bin: str) -> bool:
        return self.repository.exists_by_company_bin(company_bin)