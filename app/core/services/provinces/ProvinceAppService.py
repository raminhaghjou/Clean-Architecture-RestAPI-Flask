from app.core.services.provinces.contract import ProvinceService
from app.core.services.provinces.contract.ProvinceRepository import ProvinceRepository
from app.infrastructure.persistence import DBSession


class ProvinceAPPService(ProvinceService.ProvinceService):
    """
        This class is responsible for creating a new City
    """

    def __init__(self, repository: ProvinceRepository):
        self.repository = repository

    def add(self, province):
        return self.repository.save(province)

    def get(self, province_id):
        self.repository.get(province_id)
