import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.city_distance import CityDistanceCreate, CityDistanceRead, CityDistanceUpdate
from app.services.city_distance import CityDistanceAlreadyExistsError, CityDistanceNotFoundError, CityDistanceService

router = APIRouter(prefix="/city-distances", tags=["city distances"])


@router.get("/", response_model=list[CityDistanceRead])
def get_city_distances(db: Session = Depends(get_db)):
    service = CityDistanceService(db)
    return service.get_all_city_distances()


@router.get("/{city_distance_id}", response_model=CityDistanceRead)
def get_city_distance(city_distance_id: uuid.UUID, db: Session = Depends(get_db)):
    service = CityDistanceService(db)
    try:
        return service.get_city_distance_by_id(city_distance_id)
    except CityDistanceNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


@router.post("/", response_model=CityDistanceRead, status_code=status.HTTP_201_CREATED)
def create_city_distance(city_distance_in: CityDistanceCreate, db: Session = Depends(get_db)):
    service = CityDistanceService(db)
    try:
        return service.create_city_distance(city_distance_in)
    except CityDistanceAlreadyExistsError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.put("/{city_distance_id}", response_model=CityDistanceRead)
def update_city_distance(
    city_distance_id: uuid.UUID,
    city_distance_in: CityDistanceUpdate,
    db: Session = Depends(get_db),
):
    service = CityDistanceService(db)
    try:
        return service.update_city_distance(city_distance_id, city_distance_in)
    except CityDistanceNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
    except CityDistanceAlreadyExistsError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )