import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models.employee import Employee
from app.models.company import Company
from app.schemas.employee import EmployeeCreate, EmployeeRead, EmployeeUpdate


router = APIRouter(prefix="/employees", tags=["Employees"])


@router.post("/", response_model=EmployeeRead)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    company = db.query(Company).filter(Company.id == employee.company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    db_employee = Employee(
        last_name=employee.last_name,
        first_name=employee.first_name,
        middle_name=employee.middle_name,
        company_id=employee.company_id,
        birth_date=employee.birth_date,
        gender=employee.gender,
        id_number=employee.id_number,
        phone=employee.phone,
        email=employee.email,
        address=employee.address,
        job_position=employee.job_position,
        hire_date=employee.hire_date,
        marital_status=employee.marital_status,
        status=employee.status,
    )

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee


@router.get("/", response_model=list[EmployeeRead])
def get_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()


@router.get("/{employee_id}", response_model=EmployeeRead)
def get_employee(employee_id: uuid.UUID, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee


@router.put("/{employee_id}", response_model=EmployeeRead)
def update_employee(
    employee_id: uuid.UUID,
    employee_update: EmployeeUpdate,
    db: Session = Depends(get_db),
):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    if employee_update.company_id is not None:
        company = db.query(Company).filter(Company.id == employee_update.company_id).first()
        if not company:
            raise HTTPException(status_code=404, detail="Company not found")

    update_data = employee_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(employee, field, value)

    db.commit()
    db.refresh(employee)

    return employee


@router.delete("/{employee_id}", status_code=204)
def delete_employee(employee_id: uuid.UUID, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(employee)
    db.commit()