from abc import ABC, abstractmethod


class CityProvinceRepository(ABC):
    """
        This class is the interface for CityProvinceRepository
    """

    @abstractmethod
    def get(self, city_province_id):
        pass

    @abstractmethod
    def save(self, city: str, province: str):
        pass


