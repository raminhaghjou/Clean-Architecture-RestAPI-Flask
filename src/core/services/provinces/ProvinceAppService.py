from src.core.entities.Province import Province
from src.core.services.provinces.contract import ProvinceService
from src.core.services.provinces.contract.ProvinceRepository import ProvinceRepository
from src.core.services.provinces.dtos.AddProvinceDTO import AddProvinceDTO
from src.infrastructure.persistence.UnitOfWork import UnitOfWork


class ProvinceAPPService(ProvinceService.ProvinceService):
    """
        This class is responsible for creating a new City
    """

    def __init__(self, repository: ProvinceRepository, unitOfWork: UnitOfWork):
        self.repository = repository
        self.unitOfWork = unitOfWork

    def add(self, province: AddProvinceDTO):
        province_mod = Province(name=province.name)
        if self.repository.exist_name(province_mod) is False:
            province_model = self.repository.add(province_mod)
            self.unitOfWork.commit()
            return province_model.province_id
        else:
            raise Exception("Province %s already exists" % province.name)

    def get(self, province_id):
        return self.repository.get(province_id)
