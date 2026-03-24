import uuid

from sqlalchemy.orm import Session

from app.models import Company


class CompanyRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Company]:
        return self.db.query(Company).order_by(Company.name).all()

    def get_by_id(self, company_id: uuid.UUID) -> Company | None:
        return self.db.query(Company).filter(Company.id == company_id).first()

    def get_by_company_bin(self, company_bin: str) -> Company | None:
        return self.db.query(Company).filter(Company.company_bin == company_bin).first()

    def create(self, company: Company) -> Company:
        self.db.add(company)
        return company

    def update(self, company: Company) -> Company:
        return company

    def delete(self, company: Company) -> None:
        self.db.delete(company)

    def exists_by_id(self, company_id: uuid.UUID) -> bool:
        return self.db.query(Company.id).filter(Company.id == company_id).first() is not None

    def exists_by_company_bin(self, company_bin: str) -> bool:
        return (
            self.db.query(Company.id)
            .filter(Company.company_bin == company_bin)
            .first()
            is not None
        )