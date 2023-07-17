import jsonpickle

from flask import Blueprint, request
from flask_restful import Resource, Api
from app.core.services.cities.CityAppService import CityAPPService
from app.infrastructure.persistence import DBSession
from app.infrastructure.persistence.UnitOfWork import UnitOfWork
from app.infrastructure.persistence.cities.MySQLCityRepository import MySQLCityRepository
from app.infrastructure.persistence.provinces import MySQLProvinceRepository


class AddCityAPI(Resource):
    def post(self):
        city = request.form['city']
        province_id = request.form['province_id']
        
        
        city_repository = MySQLCityRepository(DBSession)
        city_province = CityAPPService(city_repository, DBSession)
        a = city_province.add(city, int(province_id))
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
