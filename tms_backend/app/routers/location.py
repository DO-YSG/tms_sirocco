import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.location import Location
from app.schemas.location import LocationCreate, LocationRead, LocationUpdate
from app.models.city import City
from app.dependencies import get_db


router = APIRouter(prefix="/locations", tags=["Locations"])


@router.post("/", response_model=LocationRead)
def create_location(location: LocationCreate, db: Session = Depends(get_db)):
    city = db.query(City).filter(City.id == location.city_id).first()
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    
    db_location = Location(
        name=location.name,
        location_type=location.location_type,
        city_id=location.city_id,
        address_line=location.address_line,
        comment=location.comment,
    )

    db.add(db_location)
    db.commit()
    db.refresh(db_location)

    return db_location


@router.get("/", response_model=list[LocationRead])
def get_locations(db: Session = Depends(get_db)):
    return db.query(Location).all()


@router.get("/{location_id}", response_model=LocationRead)
def get_location(location_id: uuid.UUID, db: Session = Depends(get_db)):
    location = db.query(Location).filter(Location.id == location_id).first()

    if not location:
        raise HTTPException(status_code=404, detail="Location not found")

    return location


@router.put("/{location_id}", response_model=LocationRead)
def update_location(
    location_id: uuid.UUID,
    location_update: LocationUpdate,
    db: Session = Depends(get_db),
):
    location = db.query(Location).filter(Location.id == location_id).first()

    if not location:
        raise HTTPException(status_code=404, detail="Location not found")

    update_data = location_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(location, field, value)

    db.commit()
    db.refresh(location)

    return location


@router.delete("/{location_id}", status_code=204)
def delete_location(location_id: uuid.UUID, db: Session = Depends(get_db)):
    location = db.query(Location).filter(Location.id == location_id).first()

    if not location:
        raise HTTPException(status_code=404, detail="Location not found")

    db.delete(location)
    db.commit()