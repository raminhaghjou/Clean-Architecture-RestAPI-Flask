from app.core.services.cities.contract import CityService
from app.core.services.cities.contract.CityRepository import CityRepository


class CityAPPService(CityService):
    """
        This class is responsible for creating a new City
    """

    def __init__(self, repository: CityRepository):
        self.repository = repository

    def add(self, city, province_id):
        return self.repository.save(city, province_id)

    def get(self, city_id):
        self.repository.get(city_id)
