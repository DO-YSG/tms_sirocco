import uuid

from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field, EmailStr

from app.models.employee import MaritalStatus, JobPosition, Gender


class EmployeeBase(BaseModel):
    last_name: str = Field(..., max_length=50)
    first_name: str = Field(..., max_length=50)
    middle_name: Optional[str] = Field(None, max_length=50)

    company_id: uuid.UUID

    birth_date: date
    gender: Optional[Gender] = None
    id_number: str = Field(..., max_length=20)

    phone: Optional[str] = Field(None, max_length=20)
    email: Optional[EmailStr] = None
    address: Optional[str] = Field(None, max_length=200)

    job_position: JobPosition
    hire_date: date
    marital_status: Optional[MaritalStatus] = None
    status: bool = True


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(BaseModel):
    last_name: Optional[str] = Field(None, max_length=50)
    first_name: Optional[str] = Field(None, max_length=50)
    middle_name: Optional[str] = Field(None, max_length=50)

    company_id: Optional[uuid.UUID] = None

    birth_date: Optional[date] = None
    gender: Optional[Gender] = None
    id_number: Optional[str] = Field(None, max_length=20)

    phone: Optional[str] = Field(None, max_length=20)
    email: Optional[EmailStr] = None
    address: Optional[str] = Field(None, max_length=200)

    job_position: Optional[JobPosition] = None
    hire_date: Optional[date] = None
    marital_status: Optional[MaritalStatus] = None
    status: Optional[bool] = None


class EmployeeRead(EmployeeBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    created_by: Optional[uuid.UUID] = None
    updated_by: Optional[uuid.UUID] = None

    class Config:
        from_attributes = True