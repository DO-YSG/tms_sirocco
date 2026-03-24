import uuid

from sqlalchemy.orm import Session

from app.models import CompanyRole
from app.models.company_role import CompanyRoleList


class CompanyRoleRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_company(self, company_id: uuid.UUID) -> list[CompanyRole]:
        return (
            self.db.query(CompanyRole)
            .filter(CompanyRole.company_id == company_id)
            .all()
        )

    def get_by_id(self, role_id: uuid.UUID) -> CompanyRole | None:
        return (
            self.db.query(CompanyRole)
            .filter(CompanyRole.id == role_id)
            .first()
        )

    def exists(self, company_id: uuid.UUID, role: CompanyRoleList) -> bool:
        return (
            self.db.query(CompanyRole)
            .filter(
                CompanyRole.company_id == company_id,
                CompanyRole.role == role,
            )
            .first()
            is not None
        )

    def add(self, company_role: CompanyRole) -> CompanyRole:
        self.db.add(company_role)
        return company_role

    def delete(self, company_role: CompanyRole) -> None:
        self.db.delete(company_role)