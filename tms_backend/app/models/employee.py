import enum

from app.core.database import Base
from app.models.base import BaseModelMixin

from sqlalchemy import Column, String, Enum, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Gender(str, enum.Enum):
    male = "male"
    female = "femail"
    other = "other"

class JobPosition(str, enum.Enum):
    director = "director"
    ceo = "ceo"
    accountant = "accountant"
    dispatcher = "dispetcher"
    logistician = "logistician"
    manager = "manager"
    hr_manager = "hr_manager"
    head = "head"
    mechanic = "mechanic"
    driver = "driver"

class MaritalStatus(str, enum.Enum):
    single = "single"
    married = "married"
    divorced = "divorced"
    widowed = "widowed"

class EmployeeStatus(str, enum.Enum):
    internship = "internship"
    probation = "probation"
    active = "active"
    vacation = "vacation"
    sick_leave = "sick_leave"
    dismissed = "dismissed"


class Employee(Base, BaseModelMixin):
    __tablename__ = "employees"

    company_id = Column(UUID(as_uuid=True), ForeignKey("companies.id"), nullable=False)

    last_name = Column(String(255), nullable=False)
    first_name = Column(String(255), nullable=False)
    middle_name = Column(String(255), nullable=True)
    
    birth_date = Column(Date, nullable=False)
    gender = Column(Enum(Gender, name="gender_enum"), nullable=False)
    id_number = Column(String(20), unique=True, nullable=False) # ИИН
    
    phone = Column(String(20), nullable=True)
    email = Column(String(255), unique=True, nullable=True)
    address = Column(String(255), nullable=True)

    job_position = Column(Enum(JobPosition, name="job_position_enum"), nullable=False)
    hire_date = Column(Date, nullable=False)
    marital_status = Column(Enum(MaritalStatus, name="marital_status_enum"), nullable=True)
    
    status = Column(Enum(EmployeeStatus, name = "employee_status_enum"), default=EmployeeStatus.active, nullable=False)