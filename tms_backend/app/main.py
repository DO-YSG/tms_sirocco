from fastapi import FastAPI
from app.core.database import engine, Base

from app.routers.country import router as country_router
from app.routers.city import router as city_router
from app.routers.company import router as company_router
from app.routers.company_role import router as company_role_router
from app.routers.company_account import router as company_account_router

from app.routers.vehicle import router as vehicle_router
from app.routers.location import router as location_router
from app.routers.employee import router as employee_router

app = FastAPI(title="SIROCCO", version="0.1.0")

app.include_router(country_router)
app.include_router(city_router)
app.include_router(company_router)
app.include_router(company_role_router)
app.include_router(company_account_router)

# app.include_router(vehicle_router)
# app.include_router(location_router)
# app.include_router(employee_router)

Base.metadata.create_all(bind=engine)