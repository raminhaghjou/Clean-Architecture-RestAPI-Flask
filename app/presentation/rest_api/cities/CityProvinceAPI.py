import jsonpickle

from flask import Blueprint, request
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from app.core.services.cities.CityProvinceAppService import CityProvinceAPPService
from app.infrastructure.presenters.FileCityProvinceRepository import FileCityProvinceRepository

city_blueprint = Blueprint('city', __name__)


@city_blueprint.route('/add-city', methods=["POST"])
def save_city_province():
    city = request.form['city']
    province = request.form['province']

    city_province = CityProvinceAPPService(FileCityProvinceRepository())
    a = city_province.add(city, province)

    return str(a)


@city_blueprint.route('/get-city', methods=['GET'])
def get_city_province():
    city_province_id = request.args.get('id')

    city_province = CityProvinceAPPService(FileCityProvinceRepository())
    return city_province.get(city_province_id)
