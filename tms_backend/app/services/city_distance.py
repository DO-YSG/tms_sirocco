import uuid
from typing import Sequence

from sqlalchemy.orm import Session

from app.models.city_distance import CityDistance
from app.repositories.city_distance import CityDistanceRepository
from app.schemas.city_distance import CityDistanceCreate, CityDistanceUpdate


class CityDistanceNotFoundError(Exception):
    pass


class CityDistanceAlreadyExistsError(Exception):
    pass


class CityDistanceService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = CityDistanceRepository(db)

    def get_all_city_distances(self) -> Sequence[CityDistance]:
        return self.repository.get_all()

    def get_city_distance_by_id(self, city_distance_id: uuid.UUID) -> CityDistance:
        city_distance = self.repository.get_by_id(city_distance_id)
        if not city_distance:
            raise CityDistanceNotFoundError("City distance not found")
        return city_distance

    def create_city_distance(self, data: CityDistanceCreate) -> CityDistance:
        city1_id, city2_id = sorted([data.city1_id, data.city2_id], key=str)

        normalized_data = CityDistanceCreate(
            city1_id=city1_id,
            city2_id=city2_id,
            distance_km=data.distance_km,
        )

        if self.repository.exists_by_cities(normalized_data.city1_id, normalized_data.city2_id):
            raise CityDistanceAlreadyExistsError("Distance between these cities already exists")

        try:
            city_distance = self.repository.create(normalized_data)
            self.db.commit()
            self.db.refresh(city_distance)
            return city_distance
        except Exception:
            self.db.rollback()
            raise

    def update_city_distance(self, city_distance_id: uuid.UUID, data: CityDistanceUpdate) -> CityDistance:
        city_distance = self.repository.get_by_id(city_distance_id)
        if not city_distance:
            raise CityDistanceNotFoundError("City distance not found")

        new_city1_id = data.city1_id if data.city1_id is not None else city_distance.city1_id
        new_city2_id = data.city2_id if data.city2_id is not None else city_distance.city2_id

        if new_city1_id == new_city2_id:
            raise ValueError("city1_id and city2_id must be different")

        new_city1_id, new_city2_id = sorted([new_city1_id, new_city2_id], key=str)

        existing_city_distance = self.repository.get_by_cities(new_city1_id, new_city2_id)
        if existing_city_distance and existing_city_distance.id != city_distance.id:
            raise CityDistanceAlreadyExistsError("Distance between these cities already exists")

        normalized_data = CityDistanceUpdate(
            city1_id=new_city1_id,
            city2_id=new_city2_id,
            distance_km=data.distance_km,
        )

        try:
            city_distance = self.repository.update(city_distance, normalized_data)
            self.db.commit()
            self.db.refresh(city_distance)
            return city_distance
        except Exception:
            self.db.rollback()
            raise