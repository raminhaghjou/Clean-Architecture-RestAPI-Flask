from typing import Optional
import uuid
from sqlalchemy.exc import IntegrityError
from app.core.services.provinces.contract.ProvinceRepository import ProvinceRepository
from app.core.entities.Province import Province
from app.infrastructure.persistence import DBSession
from app.infrastructure.persistence.provinces.ProvinceDBModelConfig import ProvinceDBModelConfig
from app.presentation.rest_api.config.ErrorClasses import UniqueViolationError
from app.infrastructure.persistence.UnitOfWork import UnitOfWork


class MySQLProvinceRepository(ProvinceRepository):
    """ MySQL Repository for Province
    """
    def __init__(self) -> None:
        self.__session = DBSession

    def __db_to_entity(
            self, db_row: ProvinceDBModelConfig
    ) -> Optional[Province]:
        return Province(
            province_id=db_row.province_id,
            name=db_row.name
        )

    def save(self, name: str) -> Optional[Province]:
        """ Create Province
        :param name: str
        :return: Optional[Province]
        """
        province_db_model = ProvinceDBModelConfig(
            name=name
        )

        try:
            with UnitOfWork as uow:
                with uow.get_session() as session:
                    session.add(province_db_model)
                    session.commit()
                    session.refresh(province_db_model)
        except IntegrityError as exception:
            if "violates unique constraint" in str(exception.orig):
                raise UniqueViolationError(
                    "Profession with the same name already exists"
                ) from exception
            raise

        if province_db_model is not None:
            return self.__db_to_entity(province_db_model)
        return None

    def get(self, province_id: Province.province_id) -> Optional[Province]:
        """ Get Province by id
        :param province_id: ProvinceId
        :return: Optional[Province]
        """
        result = self.__session.query(ProvinceDBModelConfig).get(province_id)
        if result is not None:
            return self.__db_to_entity(result)
        return None