from src.core.services.provinces.contract import ProvinceService
from src.core.services.provinces.contract.ProvinceRepository import ProvinceRepository
from src.infrastructure.persistence.UnitOfWork import UnitOfWork


class ProvinceAPPService(ProvinceService.ProvinceService):
    """
        This class is responsible for creating a new City
    """

    def __init__(self, repository: ProvinceRepository, unitOfWork: UnitOfWork):
        self.repository = repository
        self.unitOfWork = unitOfWork

    def add(self, province):
        with self.unitOfWork as uow:
            if self.repository.exist_name(province) is False:
                province_model = self.repository.save(province)
                uow.commit()
                uow.session.refresh(province_model)
                id = province_model
                return id
            else:
                raise Exception("Province %s already exists" % province)

    def get(self, province_id):
        return self.repository.get(province_id)
