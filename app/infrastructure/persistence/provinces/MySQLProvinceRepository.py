from typing import Optional
import uuid
from sqlalchemy.exc import IntegrityError
from sqlalchemy import literal
from app.core.services.provinces.contract.ProvinceRepository import ProvinceRepository
from app.core.entities.Province import Province
from app.infrastructure.persistence import DBSession
from app.infrastructure.persistence.provinces.ProvinceDBModelConfig import ProvinceDBModelConfig
from app.presentation.rest_api.config.ErrorClasses import UniqueViolationError


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
        
    def exist_name(self, province):
        result = self.__session.query(ProvinceDBModelConfig).filter(ProvinceDBModelConfig.name == province).first()
        if result is None:
            return False
        else: return True

    def save(self, name: str) -> Optional[Province]:
        """ Create Province
        :param name: str
        :return: Optional[Province]
        """
        province_db_model = ProvinceDBModelConfig(
            name=name
        )
        
        self.__session.add(province_db_model)
        
        if province_db_model is not None:
            return province_db_model
        return None

    def get(self, province_id) -> Optional[Province]:
        """ Get Province by id
        :param province_id: ProvinceId
        :return: Optional[Province]
        """
        result = self.__session.query(ProvinceDBModelConfig).filter(ProvinceDBModelConfig.province_id == province_id)
        if result is not None:
            return result.first()
        return None
