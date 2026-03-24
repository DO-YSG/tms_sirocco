from app.core.database import Base
from app.models.base import BaseModelMixin

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Country(Base, BaseModelMixin):
    __tablename__ = "countries" 
    
    name = Column(String(255), unique=True, nullable=False)
    code = Column(String(3), unique=True, nullable=False) # ISO 3166-1 alpha-3

    companies = relationship("Company", back_populates="country")
    country = relationship("City", back_populates="country")