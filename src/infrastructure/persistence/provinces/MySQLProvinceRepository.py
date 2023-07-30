from typing import Optional
from src.core.entities.Province import Province
from src.core.services.provinces.contract.ProvinceRepository import ProvinceRepository
from src.core.services.provinces.dtos.GetProvinceDTO import GetProvinceDTO
from src.infrastructure.persistence import DBSession
from src.infrastructure.persistence.provinces.ProvinceDBModelConfig import ProvinceDBModelConfig


class MySQLProvinceRepository(ProvinceRepository):
    """ MySQL Repository for Province
    """
    def __init__(self, session: DBSession):
        self.__session = session

    def __db_to_entity(
            self, db_row: ProvinceDBModelConfig
    ) -> Optional[Province]:
        return Province(
            province_id=db_row.province_id,
            name=db_row.name
        )
        
    def exist_name(self, province: Province):
        result = self.__session.query(ProvinceDBModelConfig).filter(ProvinceDBModelConfig.name == province.name).first()
        if result is None:
            return False
        else: return True

    def add(self, name: Province) -> Optional[Province]:
        """ Create Province
        :param name: Province
        :return: Optional[ProvinceDBModelConfig]
        """
        province_db_model = ProvinceDBModelConfig(
            name=name.name
        )
        
        self.__session.add(province_db_model)
        
        return province_db_model
        

    def get(self, province_id):
        """ Get Province by id
        :param province_id: ProvinceId
        :return: Optional[GetProvinceDTO]
        """
        result = self.__session.query(ProvinceDBModelConfig).filter(ProvinceDBModelConfig.province_id == province_id).first()
        
        if result is not None:
            province_dto = GetProvinceDTO(result.province_id, result.name)
            return province_dto
        return None
