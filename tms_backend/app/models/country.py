from app.core.database import Base
from app.models.base import BaseModelMixin

from sqlalchemy import Column, String


class Country(Base, BaseModelMixin):
    __tablename__ = "countries" 
    
    name = Column(String(255), unique=True, nullable=False)
    code = Column(String(3), unique=True, nullable=False) # KAZ, RUS