"""
    Entity CityProvince data Model 
"""

from datetime import date

from sqlalchemy import Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from app.infrastructure.migration.BaseModel import BaseModel
from app.infrastructure.migration.ProvinceDBModel import ProvinceDBModel


class CityDBModel(BaseModel):
    """
        Defines the City database model.
    """
    
    __tablename__ = 'cities'
    
    city_id = Mapped[int] = mapped_column(Integer, primary_key = True, nullable = False, unique = True)
    name = Mapped[str] = mapped_column(String(80), nullable = False, unique = False)
    province_id = Mapped[int] = mapped_column(Integer, ForeignKey('province_id.province_id'), nullable = False)
    province = Mapped["ProvinceDBModel"] = relationship(back_populates= 'cities')
