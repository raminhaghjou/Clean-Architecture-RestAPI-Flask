
from abc import ABC, abstractmethod

from app.core.services.cities.contract import CityRepository
from app.core.services.provinces.contract import ProvinceRepository


class UnitOfWorkBase(ABC):
    cities: CityRepository
    provinces: ProvinceRepository

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.rollback()

    @abstractmethod
    def commit(self):
        raise NotImplementedError()

    @abstractmethod
    def rollback(self):
        raise NotImplementedError()