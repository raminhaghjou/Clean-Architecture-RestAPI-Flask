import jsonpickle

from flask import Blueprint, request
from flask_restful import Resource, Api
from app.core.services.cities.CityAppService import CityAPPService
from app.infrastructure.persistence.FileCityRepository import FileCityRepository


class AddCityAPI(Resource):
    def post(self):
        city = request.form['name']
        province = request.form['province_id']

        city_province = CityAPPService(FileCityRepository())
        a = city_province.add(city, province)

        return str(a)


class CityAPI(Resource):
    def get(self):
        city_province_id = request.args.get('id')

        city_province = CityAPPService(FileCityRepository())
        return city_province.get(city_province_id)

    def delete(self):
        city_province_id = request.args.get('id')

        city_province = CityAPPService(FileCityRepository())
        return city_province.delete(city_province_id)


city_api = Blueprint('rest_api/cities/name', __name__)
api = Api(city_api)
api.add_resource(AddCityAPI, '/cities', endpoint='cities')
api.add_resource(CityAPI, '/cities/<int:id>', endpoint='name')
