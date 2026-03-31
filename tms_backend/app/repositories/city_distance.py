import uuid
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import CityDistance
from app.schemas.city_distance import CityDistanceCreate, CityDistanceUpdate


class CityDistanceRepository:  
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> Sequence[CityDistance]:
        stmt = select(CityDistance).order_by(CityDistance.distance_km)
        return self.db.execute(stmt).scalars().all()

    def get_by_id(self, city_distance_id: uuid.UUID) -> CityDistance | None:
        stmt = select(CityDistance).where(CityDistance.id == city_distance_id)
        return self.db.execute(stmt).scalar_one_or_none()

    def get_by_cities(self, city1_id: uuid.UUID, city2_id: uuid.UUID) -> CityDistance | None:
        stmt = select(CityDistance).where(
            CityDistance.city1_id == city1_id,
            CityDistance.city2_id == city2_id,
        )
        return self.db.execute(stmt).scalar_one_or_none()

    def exists_by_id(self, city_distance_id: uuid.UUID) -> bool:
        stmt = select(CityDistance.id).where(CityDistance.id == city_distance_id)
        return self.db.execute(stmt).first() is not None

    def exists_by_cities(self, city1_id: uuid.UUID, city2_id: uuid.UUID) -> bool:
        stmt = select(CityDistance.id).where(
            CityDistance.city1_id == city1_id,
            CityDistance.city2_id == city2_id,
        )
        return self.db.execute(stmt).first() is not None

    def create(self, data: CityDistanceCreate) -> CityDistance:
        city_distance = CityDistance(**data.model_dump())
        self.db.add(city_distance)
        return city_distance

    def update(self, city_distance: CityDistance, data: CityDistanceUpdate) -> CityDistance:
        update_data = data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(city_distance, field, value)

        return city_distance