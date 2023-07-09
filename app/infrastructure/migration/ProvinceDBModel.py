"""
    Entity CityProvince data Model 
"""

from datetime import date

from sqlalchemy import Column, Date, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import BIGINT
from app.infrastructure.migration.BaseModel import BaseModel
from app.infrastructure.migration.CityDBModel import CityDBModel


class ProvinceDBModel(BaseModel):
    """
        Defines the Province database model.
    """
    
    __tablename__ = 'provinces'
    
    province_id = Mapped[int] = mapped_column(Integer, primary_key = True, nullable = False, unique = True)
    name = Mapped[str] = mapped_column(String(80), nullable = False, unique = False)
    cities = Mapped["CityDBModel"] = relationship(back_populates= 'province_id')
