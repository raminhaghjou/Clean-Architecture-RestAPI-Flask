
from flask import Blueprint, jsonify, make_response, request
from flask_restful import Api, Resource

from app.core.services.cities.CityAppService import CityAPPService
from app.infrastructure.persistence import DBSession
from app.infrastructure.persistence.cities.MySQLCityRepository import \
    MySQLCityRepository
from app.infrastructure.persistence.UnitOfWork import UnitOfWork


class AddCityAPI(Resource):
    def post(self):
        city = request.get_json()['city']
        province_id = request.get_json()['province_id']
        
        uow = UnitOfWork(DBSession)
        city_repository = MySQLCityRepository(DBSession)
        city_service = CityAPPService(city_repository, uow)
        city_id = city_service.add(city, province_id)
        
        response = make_response(
            jsonify(
                {"id": str(city_id)}
            ),
            200,
        )
        response.headers["Content-Type"] = "application/json"
        return response


class CityAPI(Resource):
    def get(self):
        city_id = request.get_json()['id']

        city = CityAPPService(MySQLCityRepository())
        city = city.get(city_id)
        response = make_response(
            jsonify(
                {"name": str(city)}
            ),
            200,
        )
        response.headers["Content-Type"] = "application/json"
        return response

    def delete(self):
        city_id = request.get_json()['id']

        city = CityAPPService(MySQLCityRepository())
        city.delete(city_id)
        response = make_response(
            jsonify(
                {"message": "city deleted successfully"}
            ),
            200,
        )
        response.headers["Content-Type"] = "application/json"
        return response


city_api = Blueprint('rest_api/cities/name', __name__)
api = Api(city_api)
api.add_resource(AddCityAPI, '/cities', endpoint='cities')
api.add_resource(CityAPI, '/cities/<int:id>', endpoint='name')
