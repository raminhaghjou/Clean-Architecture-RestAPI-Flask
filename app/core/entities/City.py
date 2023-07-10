# from app.core.value_objects import CityProvinceId


class City:
    """
        Definition of the CityProvince entity
    """
    # city_id: int
    # name: str
    # province_id: int

    def __init__(self, city_id, name, province_id):
        self.name = name
        self.province_id = province_id
        self.city_id = city_id
