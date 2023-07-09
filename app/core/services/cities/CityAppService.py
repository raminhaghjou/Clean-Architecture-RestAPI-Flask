from app.core.services.cities.contract.CityRepository import CityRepository


class CityAPPService:
    """
        This class is responsible for creating a new cityprovince
    """

    def __init__(self, repository: CityRepository):
        self.repository = repository

    def add(self, city, province):
        return self.repository.save(city, province)

    def get(self, city_province_id):
        self.repository.get(city_province_id)
