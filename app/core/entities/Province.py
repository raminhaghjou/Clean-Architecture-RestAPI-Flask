# from app.core.value_objects import CityProvinceId


class Province:
    """
        Definition of the CityProvince entity
    """
    province_id: int
    name: str

    def __init__(self, province_id, name):
        self.name = name
        self.province_id = province_id
