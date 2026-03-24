import uuid
from typing import Optional

from app.schemas.base import ORMBaseSchema, BaseReadSchema
from app.models.company_role import CompanyRoleList


class CompanyRoleBase(ORMBaseSchema):
    role: CompanyRoleList
    note: Optional[str] = None


class CompanyRoleCreate(CompanyRoleBase):
    pass


class CompanyRoleRead(CompanyRoleBase, BaseReadSchema):
    company_id: uuid.UUID