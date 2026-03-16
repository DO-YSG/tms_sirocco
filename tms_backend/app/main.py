from fastapi import FastAPI
from app.core.database import engine, Base

from app.models.company import Company
from app.models.vehicle import Vehicle
from app.models.employee import Employee

from app.routers.vehicle import router as vehicle_router
from app.routers.company import router as company_router
from app.routers.city import router as city_router
from app.routers.location import router as location_router
from app.routers.employee import router as employee_router

app = FastAPI()

app.include_router(vehicle_router)
app.include_router(company_router)
app.include_router(city_router)
app.include_router(location_router)
app.include_router(employee_router)

Base.metadata.create_all(bind=engine)