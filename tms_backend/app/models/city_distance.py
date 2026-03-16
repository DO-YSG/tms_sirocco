from app.core.database import Base
from app.models.base import BaseModelMixin

from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID


class CityDistance(Base, BaseModelMixin):
    __tablename__ = "city_distances"

    city1_id = Column(UUID(as_uuid=True), ForeignKey("cities.id"), nullable=False)
    city2_id = Column(UUID(as_uuid=True), ForeignKey("cities.id"), nullable=False)

    distance_km = Column(Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint("city1_id", "city2_id", name="uq_city_distance"),
        CheckConstraint("city1_id <> city2_id", name="ck_city_distance_not_same_city"),
        CheckConstraint("distance_km > 0", name="ck_city_distance_positive"),
    )