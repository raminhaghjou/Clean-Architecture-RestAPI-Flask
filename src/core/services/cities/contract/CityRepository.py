from abc import ABC, abstractmethod


class CityRepository(ABC):
    """
        This class is the interface for CityRepository
    """

    @abstractmethod
    def get(self, city_id: int):
        pass

    @abstractmethod
    def add(self, city: str, province_id: int):
        pass

    @abstractmethod
    def exist_name(self, province: str):
        pass

