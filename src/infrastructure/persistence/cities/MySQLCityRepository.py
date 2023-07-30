from typing import Optional
from src.core.entities.City import City
from src.core.services.cities.contract.CityRepository import CityRepository
from src.core.services.cities.dtos.GetCityDTO import GetCityDTO
from src.infrastructure.persistence import DBSession
from src.infrastructure.persistence.cities.CityDBModelConfig import CityDBModelConfig


class MySQLCityRepository(CityRepository):
    """ MySQL Repository for City
    """
    def __init__(self, session: DBSession):
        self.__session = session
    
    def exist_name(self, city: City):
        result = self.__session.query(CityDBModelConfig).filter(CityDBModelConfig.name == city.name, CityDBModelConfig.province_id == city.province_id).first()
        if result is None:
            return False
        else: return True

    def add(self, city: City) -> Optional[City]:
        """ Create City
        :param city: City
        :return: Optional[CityDBModelConfig]
        """
        city_db_model = CityDBModelConfig(
            name=city.name,
            province_id=city.province_id
        )
        
        self.__session.add(city_db_model)
        
        return city_db_model
        

    def get(self, city_id):
        """ Get City by id
        :param city_id: CityId
        :return: Optional[GetCityDTO]
        """
        result = self.__session.query(CityDBModelConfig).filter(CityDBModelConfig.city_id == city_id).first()
        
        if result is not None:
            city_dto = GetCityDTO(result.city_id, result.name, result.province_id)
            return city_dto
        return None
