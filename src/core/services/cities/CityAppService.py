from src.core.entities.City import City
from src.core.services.cities.contract import CityService
from src.core.services.cities.contract.CityRepository import CityRepository
from src.core.services.cities.dtos.AddCityDTO import AddCityDTO
from src.infrastructure.persistence.UnitOfWork import UnitOfWork


class CityAPPService(CityService.CityService):
    """
        This class is responsible for creating a new City
    """

    def __init__(self, repository: CityRepository, unitOfWork: UnitOfWork):
        self.repository = repository
        self.unitOfWork = unitOfWork

    def add(self, city: AddCityDTO):
        city_mod = City(name=city.name, province_id=city.province_id)
        if self.repository.exist_name(city_mod) is False:
            city_model = self.repository.add(city_mod)
            self.unitOfWork.commit()
            return city_model.city_id
        else:
            raise Exception("City %s already exists" % city.name)

    def get(self, city_id):
        return self.repository.get(city_id)
