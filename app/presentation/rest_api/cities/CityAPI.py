import jsonpickle

from flask import Blueprint, request
from flask_restful import Resource, Api
from app.core.services.cities.CityAppService import CityAPPService
from app.core.services.provinces.ProvinceAppService import ProvinceAPPService
from app.infrastructure.persistence import DBSession
from app.infrastructure.persistence.UnitOfWork import UnitOfWork
from app.infrastructure.persistence.cities.MySQLCityRepository import MySQLCityRepository
from app.infrastructure.persistence.provinces.MySQLProvinceRepository import MySQLProvinceRepository


class AddCityAPI(Resource):
    def post(self):
        city = request.form['city']
        province = request.form['province']
        
        
        city_repository = MySQLCityRepository(DBSession)
        province_repository = MySQLProvinceRepository(DBSession)
        province_service = ProvinceAPPService(province_repository)
        province_id = province_service.add(province)
        city_service = CityAPPService(city_repository)
        a = city_service.add(city, province_id)
        # a = CityAPPService(CityRepository()).add(city=city, province_id=int(province))

        return str(a)


class CityAPI(Resource):
    def get(self):
        city_province_id = request.args.get('id')

        city_province = CityAPPService(MySQLCityRepository())
        return city_province.get(city_province_id)

    def delete(self):
        city_province_id = request.args.get('id')

        city_province = CityAPPService(MySQLCityRepository())
        return city_province.delete(city_province_id)


city_api = Blueprint('rest_api/cities/name', __name__)
api = Api(city_api)
api.add_resource(AddCityAPI, '/cities', endpoint='cities')
api.add_resource(CityAPI, '/cities/<int:id>', endpoint='name')
