import copy
import uuid
from typing import Dict
from app.core.value_objects import CityProvinceId
from app.core.services.cities.contract.CityProvinceRepository import CityProvinceRepository
from app.core.entities.City import CityProvince


class FileCityProvinceRepository(CityProvinceRepository):
    def __init__(self):
        self._city_province_list: Dict[CityProvinceId, CityProvince] = {}

    def get(self, city_province_id: CityProvinceId):
        return copy.deepcopy(self._city_province_list[CityProvinceId])
    
    def save(self, city: str, province: str):
        city_province = CityProvince(
            city_province_id=uuid.uuid4(),
            city=city,
            province=province
        )
        self._city_province_list[city_province.city_province_id] = city_province
        return self._city_province_list[city_province.city_province_id].city_province_id
