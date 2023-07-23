from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from src.infrastructure.persistence.cities.CityDBModelConfig import CityDBModelConfig


class CitySchema(SQLAlchemySchema):
    class meta:
        model = CityDBModelConfig
        include_fk = True
        load_instance = True
        
    city_id = auto_field(column_name="city_id", model=meta.model)
    name = auto_field(column_name="name", model=meta.model)
    province_id = auto_field(column_name="province_id", model=meta.model)
    