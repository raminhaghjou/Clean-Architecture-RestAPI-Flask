from app.core.services.cities.contract.CityProvinceRepository import CityProvinceRepository


class CityProvinceAPPService:
    """
        This class is responsible for creating a new cityprovince
    """

    def __init__(self, repository: CityProvinceRepository):
        self.repository = repository

    def add(self, city, province):
        return self.repository.save(city, province)

    def get(self, city_province_id):
        self.repository.get(city_province_id)
