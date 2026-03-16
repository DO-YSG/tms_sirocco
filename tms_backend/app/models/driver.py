from app.core.database import Base
from app.models.base import BaseModelMixin

from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Driver(Base, BaseModelMixin):
    __tablename__ = "drivers"

    employee_id = Column(UUID(as_uuid=True), ForeignKey("employees.id"), unique=True, nullable=False)

    experience_years = Column(Integer, nullable=True)

    # данные водительского удостоверения
    # данные карточки тахографа
    # данные шоферской мед. комиссии

    note = Column(Text, nullable=True)