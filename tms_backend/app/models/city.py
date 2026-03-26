from app.core.database import Base
from app.models.base import BaseModelMixin

from sqlalchemy import Column, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID


class City(Base, BaseModelMixin):
    __tablename__ = "cities" 
    
    name = Column(String(255), nullable=False, index=True)
    region = Column(String(255), nullable=False)
    country_id = Column(UUID(as_uuid=True), ForeignKey("countries.id"), nullable=False, index=True)

    country = relationship("Country", back_populates="cities")
    companies = relationship("Company", back_populates="city")

    __table_args__ = (
        UniqueConstraint("name", "region", "country_id", name="uq_name_region_country"),
    )