import jsonpickle

from flask import Blueprint, request
from flask_restful import Resource, Api
from app.core.services.cities.CityProvinceAppService import CityProvinceAPPService
from app.infrastructure.persistence.FileCityProvinceRepository import FileCityProvinceRepository

class AddCityProvinceAPI(Resource):
    def post(self):
        city = request.form['city']
        province = request.form['province']

        city_province = CityProvinceAPPService(FileCityProvinceRepository())
        a = city_province.add(city, province)

        return str(a)


class City(Resource):
    def get(self):
        city_province_id = request.args.get('id')

        city_province = CityProvinceAPPService(FileCityProvinceRepository())
        return city_province.get(city_province_id)

    def delete(self):
        city_province_id = request.args.get('id')

        city_province = CityProvinceAPPService(FileCityProvinceRepository())
        return city_province.delete(city_province_id)


city_api = Blueprint('rest_api/cities/city', __name__)
api = Api(city_api)
api.add_resource(AddCityProvinceAPI, '/cities', endpoint='cities')
api.add_resource(City, '/cities/<int:id>', endpoint='city')