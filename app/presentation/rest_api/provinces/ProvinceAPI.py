
from flask import Blueprint, jsonify, make_response, request
from flask_restful import Resource, Api, reqparse
from app.core.services.provinces.ProvinceAppService import ProvinceAPPService
from app.infrastructure.persistence import DBSession
from app.infrastructure.persistence.UnitOfWork import UnitOfWork
from app.infrastructure.persistence.cities.CityDBModelConfig import CityDBModelConfig
from app.infrastructure.persistence.provinces.MySQLProvinceRepository import MySQLProvinceRepository


# Define parser and request args
parser = reqparse.RequestParser()


class AddProvinceAPI(Resource):
    def post(self):
        parser.add_argument('province', type=str, required=True, help='Province is required')
        args = parser.parse_args()
        province = args['province']
        # province = request.get_json()['province']
        
        uow = UnitOfWork(DBSession)
        province_repository = MySQLProvinceRepository(DBSession)
        province_service = ProvinceAPPService(province_repository, uow)
        province_id = province_service.add(province)

        response = make_response(
            jsonify(
                {"id": str(province_id)}
            ),
            200,
        )
        response.headers["Content-Type"] = "application/json"
        return response


class ProvinceAPI(Resource):
    def get(self,province_id):

        uow = UnitOfWork(DBSession)
        province_repository = MySQLProvinceRepository(DBSession)
        province = ProvinceAPPService(province_repository, uow)
        province = province.get(province_id)
        if province is None:
            response = make_response(
                jsonify(
                    {"message": "Nop for province not found"}
                ),
                204,
            )
            response.headers["Content-Type"] = "application/json"
            return response
        else:
            response = make_response(
                jsonify(
                    {"name": province.name}
                ),
                200,
            )
            response.headers["Content-Type"] = "application/json"
            return response

    def delete(self, province_id):

        uow = UnitOfWork(DBSession)
        province_repository = MySQLProvinceRepository(DBSession)
        province = ProvinceAPPService(province_repository, uow)
        province.delete(province_id)
        response = make_response(
            jsonify(
                {"message": "province deleted successfully"}
            ),
            200,
        )
        response.headers["Content-Type"] = "application/json"
        return response


province_api = Blueprint('rest_api/provinces/name', __name__)
api = Api(province_api)
api.add_resource(AddProvinceAPI, '/provinces', endpoint='provinces')
api.add_resource(ProvinceAPI, '/provinces/<int:province_id>', endpoint='provinces_id')
