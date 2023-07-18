
from flask import Blueprint, jsonify, make_response, request
from flask_restful import Resource, Api
from app.core.services.provinces.ProvinceAppService import ProvinceAPPService
from app.infrastructure.persistence import DBSession
from app.infrastructure.persistence.UnitOfWork import UnitOfWork
from app.infrastructure.persistence.provinces.MySQLProvinceRepository import MySQLProvinceRepository


class AddProvinceAPI(Resource):
    def post(self):
        province = request.get_json()['province']
        
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
    def get(self):
        province_id = request.get_json()['id']

        province = ProvinceAPPService(MySQLProvinceRepository())
        province = province.get(province_id)
        response = make_response(
            jsonify(
                {"name": str(province)}
            ),
            200,
        )
        response.headers["Content-Type"] = "application/json"
        return response

    def delete(self):
        province_id = request.get_json()['id']

        province = ProvinceAPPService(MySQLProvinceRepository())
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
api.add_resource(ProvinceAPI, '/provinces/<int:id>', endpoint='name')
