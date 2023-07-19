from typing import Optional
import uuid
from sqlalchemy.exc import IntegrityError
from sqlalchemy import literal
from app.core.services.cities.contract.CityRepository import CityRepository
from app.core.entities.City import City
from app.infrastructure.persistence import DBSession
from app.infrastructure.persistence.cities.CityDBModelConfig import CityDBModelConfig
from app.presentation.rest_api.config.ErrorClasses import UniqueViolationError


class MySQLCityRepository(CityRepository):
    """ MySQL Repository for City
    """
    def __init__(self, session: DBSession):
        self.__session = session
    
    def exist_name(self, city, province_id):
        result = self.__session.query(CityDBModelConfig).filter(CityDBModelConfig.name == city, CityDBModelConfig.province_id == province_id).first()
        if result is None:
            return False
        else: return True

    def save(self, name: str, province_id: int) -> Optional[CityDBModelConfig]:
        """ Create City
        :param name: str
        :return: Optional[City]
        """
        city_db_model = CityDBModelConfig(
            name=name,
            province_id=province_id
        )
        
        self.__session.add(city_db_model)

        if city_db_model is not None:
            return city_db_model
        return None

    def get(self, city_id) -> Optional[CityDBModelConfig]:
        """ Get City by id
        :param city_id: CityId
        :return: Optional[City]
        """
        result = self.__session.query(CityDBModelConfig).filter(CityDBModelConfig.city_id == city_id)
        if result is not None:
            return result.first()
        return None
