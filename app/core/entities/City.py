from app.core.value_objects import CityProvinceId


class CityProvince:
    """
        Difinition of the CityProvince entity
    """
    city_province_id: CityProvinceId
    city: str
    province: str

    def __init__(self, city_province_id, city, province):
        self.city = city
        self.province = province
        self.city_province_id = city_province_id
