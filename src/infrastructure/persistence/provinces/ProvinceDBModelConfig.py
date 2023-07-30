"""
    Entity CityProvince data Model 
"""

import json
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from flask_serialize import FlaskSerialize
from src.infrastructure.persistence import Base


"""create a flask-serialize mixin instance from
    the factory method `FlaskSerialize`
"""
# fs_mixin = FlaskSerialize(Base)

class ProvinceDBModelConfig(Base):
    """
        Defines the Province database model.
    """
    
    __tablename__ = 'provinces'
    
    province_id : Mapped[int] = mapped_column(Integer, primary_key = True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(80), nullable = False, unique = False)
    cities : Mapped["CityDBModelConfig"] = relationship(back_populates= 'province')
    
    def __repr__(self):
        f"{self.__class__.__name__}({self.province_id}, {self.name})"
