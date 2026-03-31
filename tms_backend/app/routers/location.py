import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.location import LocationCreate, LocationUpdate, LocationRead
from app.services.location import LocationService


router = APIRouter(prefix="/locations", tags=["locations"])


@router.post("/", response_model=LocationRead, status_code=status.HTTP_201_CREATED)
def create_location(data: LocationCreate, db: Session = Depends(get_db)):
    service = LocationService(db)
    return service.create(data)


@router.get("/{location_id}", response_model=LocationRead)
def get_location(location_id: uuid.UUID, db: Session = Depends(get_db)):
    service = LocationService(db)
    location = service.get_by_id(location_id)

    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location


@router.get("/", response_model=list[LocationRead])
def get_locations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    service = LocationService(db)
    return service.get_list(skip=skip, limit=limit)


@router.put("/{location_id}", response_model=LocationRead)
def update_location(location_id: uuid.UUID, data: LocationUpdate, db: Session = Depends(get_db)):
    service = LocationService(db)
    location = service.update(location_id, data)

    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location


@router.delete("/{location_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_location(location_id: uuid.UUID, db: Session = Depends(get_db)):
    service = LocationService(db)
    deleted = service.delete(location_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Location not found")