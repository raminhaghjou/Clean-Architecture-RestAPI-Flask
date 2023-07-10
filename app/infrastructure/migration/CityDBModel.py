"""
    Entity CityProvince data Model 
"""

from datetime import date

from sqlalchemy import Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from app.infrastructure.migration import Base
from app.infrastructure.migration.ProvinceDBModel import ProvinceDBModel


class CityDBModel(Base):
    """
        Defines the City database model.
    """
    
    __tablename__ = 'cities'
    
    city_id : Mapped[int] = mapped_column(Integer, primary_key = True, autoincrement=True, nullable = False, unique = True)
    name : Mapped[str] = mapped_column(String(80), nullable = False, unique = False)
    province_id : Mapped[int] = mapped_column(Integer, ForeignKey('provinces.province_id'), nullable = False)
    province : Mapped["ProvinceDBModel"] = relationship(back_populates= 'cities')
    
    def __init__(self, name, province_id):
        self.name = name
        self.province_id = province_id