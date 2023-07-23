from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from src.infrastructure.persistence.provinces.ProvinceDBModelConfig import ProvinceDBModelConfig

class ProvinceSchema(SQLAlchemySchema):
    class meta:
        model = ProvinceDBModelConfig
        include_relationships = True
        load_instance = True
    
    province_id = auto_field(column_name="province_id", model=meta.model)
    name = auto_field(column_name="name", model=meta.model)
    # cities = auto_field( model=meta.model)