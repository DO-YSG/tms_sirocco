import uuid

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.services.company_role import CompanyRoleService
from app.schemas.company_role import CompanyRoleCreate, CompanyRoleRead

router = APIRouter(prefix="/companies/{company_id}/roles", tags=["company roles"])


@router.get("/", response_model=list[CompanyRoleRead])
def get_company_roles(company_id: uuid.UUID, db: Session = Depends(get_db)):
    service = CompanyRoleService(db)
    return service.get_by_company(company_id)


@router.post("/", response_model=CompanyRoleRead, status_code=status.HTTP_201_CREATED)
def create_company_role(company_id: uuid.UUID, data: CompanyRoleCreate, db: Session = Depends(get_db)):
    service = CompanyRoleService(db)
    return service.create(company_id, data)


@router.delete("/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_company_role(company_id: uuid.UUID, role_id: uuid.UUID, db: Session = Depends(get_db)):
    service = CompanyRoleService(db)
    service.delete(company_id, role_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)