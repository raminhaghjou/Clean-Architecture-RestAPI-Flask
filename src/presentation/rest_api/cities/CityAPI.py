from dataclasses import asdict
import json
from flask import Blueprint, jsonify, make_response, request
from flask_restful import Api, Resource, reqparse

from src.core.services.cities.CityAppService import CityAPPService
from src.core.services.cities.dtos.AddCityDTO import AddCityDTO
from src.infrastructure.persistence import DBSession
from src.infrastructure.persistence.cities.MySQLCityRepository import \
    MySQLCityRepository
from src.infrastructure.persistence.UnitOfWork import UnitOfWork
from src.presentation.rest_api.config.CitySchema import CitySchema
from src.presentation.rest_api.config.JsonEncoder import JsonEncoder


# Define parser and request args
parser = reqparse.RequestParser()

city_schema = CitySchema()



class AddCityAPI(Resource):
    
    
    def post(self):
        # parser.add_argument('city', type=str, required=True, help='City is required')
        # parser.add_argument('province_id', type=str, required=True, help='Province_id is required')
        # args = parser.parse_args()
        # city = args['city']
        # province_id = args['province_id']
        args = request.get_json()
        city_dto = AddCityDTO(name=args['city'], province_id=args['province_id'])
        uow = UnitOfWork(DBSession)
        city_repository = MySQLCityRepository(DBSession)
        city_service = CityAPPService(city_repository, uow)
        city_id = city_service.add(city_dto)
        
        response = make_response(
            str(city_id),
            200,
        )
        response.headers["Content-Type"] = "application/json"
        return response


class CityAPI(Resource):
    def get(self, city_id):

        uow = UnitOfWork(DBSession)
        city_repository = MySQLCityRepository(DBSession)
        city = CityAPPService(city_repository, uow)
        city = city.get(city_id)
        if city is None:
            pass
        else:
            city = asdict(city)
            response = make_response(
                json.dumps(city),
                200,
            )
            response.headers["Content-Type"] = "application/json"
            return response

    def delete(self, city_id):

        uow = UnitOfWork(DBSession)
        city_repository = MySQLCityRepository(DBSession)
        city = CityAPPService(city_repository, uow)
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
api.add_resource(CityAPI, '/cities/<int:city_id>', endpoint='name')
