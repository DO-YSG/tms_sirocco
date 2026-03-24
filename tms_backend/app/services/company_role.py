import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import CompanyRole
from app.repositories.company import CompanyRepository
from app.repositories.company_role import CompanyRoleRepository
from app.schemas.company_role import CompanyRoleCreate


class CompanyRoleService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = CompanyRoleRepository(db)
        self.company_repo = CompanyRepository(db)

    def get_by_company(self, company_id: uuid.UUID) -> list[CompanyRole]:
        company = self.company_repo.get_by_id(company_id)
        if not company:
            raise HTTPException(status_code=404, detail="Company not found")

        return self.repo.get_by_company(company_id)

    def get_by_id(self, role_id: uuid.UUID) -> CompanyRole:
        role = self.repo.get_by_id(role_id)
        if not role:
            raise HTTPException(status_code=404, detail="Company role not found")
        return role

    def create(self, company_id: uuid.UUID, data: CompanyRoleCreate) -> CompanyRole:
        company = self.company_repo.get_by_id(company_id)
        if not company:
            raise HTTPException(status_code=404, detail="Company not found")

        if self.repo.exists(company_id, data.role):
            raise HTTPException(
                status_code=400,
                detail="This role already exists for this company"
            )

        try:
            company_role = CompanyRole(
                company_id=company_id,
                **data.model_dump()
            )

            self.repo.add(company_role)

            self.db.commit()
            self.db.refresh(company_role)

            return company_role

        except Exception:
            self.db.rollback()
            raise

    def delete(self, company_id: uuid.UUID, role_id: uuid.UUID) -> None:
        company_role = self.get_by_id(role_id)

        if company_role.company_id != company_id:
            raise HTTPException(status_code=404, detail="Company role not found")

        try:
            self.repo.delete(company_role)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise