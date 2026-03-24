import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.company_account import CompanyAccountRepository
from app.schemas.company_account import CompanyAccountCreate, CompanyAccountUpdate


class CompanyAccountService:

    def __init__(self, db: Session):
        self.repo = CompanyAccountRepository(db)
        self.db = db

    def get_by_company(self, company_id: uuid.UUID):
        return self.repo.get_by_company_id(company_id)

    def get_by_id(self, company_id: uuid.UUID, account_id: uuid.UUID):
        account = self.repo.get_by_id(account_id)
        if not account:
            raise HTTPException(status_code=404, detail="Company account not found")
        if account.company_id != company_id:
            raise HTTPException(status_code=404, detail="Company account not found")
        return account

    def create(self, company_id: uuid.UUID, data: CompanyAccountCreate):
        # Проверка дубликата
        existing = self.repo.get_by_company_id(company_id)
        for acc in existing:
            if acc.bank_account == data.bank_account and acc.currency == data.currency:
                raise HTTPException(
                    status_code=400,
                    detail="Account with this number and currency already exists"
                )

        # Если is_default=True — снимаем дефолт с остальных
        if data.is_default:
            for acc in existing:
                acc.is_default = False

        account = self.repo.create(company_id=company_id, **data.model_dump())
        try:
            self.db.commit()
            self.db.refresh(account)
            return account
        except Exception:
            self.db.rollback()
            raise

    def update(self, company_id: uuid.UUID, account_id: uuid.UUID, data: CompanyAccountUpdate):
        account = self.get_by_id(company_id, account_id)

        update_data = data.model_dump(exclude_unset=True)

        # Если is_default=True — снимаем дефолт с остальных
        if update_data.get("is_default"):
            existing = self.repo.get_by_company_id(company_id)
            for acc in existing:
                if acc.id != account_id:
                    acc.is_default = False

        self.repo.update(account, **update_data)
        try:
            self.db.commit()
            self.db.refresh(account)
            return account
        except Exception:
            self.db.rollback()
            raise

    def delete(self, company_id: uuid.UUID, account_id: uuid.UUID) -> None:
        account = self.get_by_id(company_id, account_id)
        self.repo.delete(account)
        try:
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise