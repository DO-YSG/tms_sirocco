import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.repositories.country import CountryRepository
from app.schemas.country import CountryRead

router = APIRouter(prefix="/countries", tags=["countries"])


@router.get("/", response_model=list[CountryRead])
def get_countries(db: Session = Depends(get_db)):
    repo = CountryRepository(db)
    return repo.get_all()


@router.get("/{country_id}", response_model=CountryRead)
def get_country(country_id: uuid.UUID, db: Session = Depends(get_db)):
    repo = CountryRepository(db)
    country = repo.get_by_id(country_id)
    if not country:
        raise HTTPException(status_code=404, detail="Country not found")
    return country