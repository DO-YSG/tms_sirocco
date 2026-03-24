# repositories/company_account.py
import uuid
from typing import Optional

from sqlalchemy.orm import Session

from app.models import CompanyAccount


class CompanyAccountRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, account_id: uuid.UUID) -> Optional[CompanyAccount]:
        return (
            self.db.query(CompanyAccount)
            .filter(CompanyAccount.id == account_id)
            .first()
        )

    def get_by_company_id(self, company_id: uuid.UUID) -> list[CompanyAccount]:
        return (
            self.db.query(CompanyAccount)
            .filter(CompanyAccount.company_id == company_id)
            .all()
        )

    def create(self, **kwargs) -> CompanyAccount:
        obj = CompanyAccount(**kwargs)
        self.db.add(obj)
        return obj

    def update(self, obj: CompanyAccount, **kwargs) -> CompanyAccount:
        for field, value in kwargs.items():
            setattr(obj, field, value)
        return obj

    def delete(self, obj: CompanyAccount) -> None:
        self.db.delete(obj)