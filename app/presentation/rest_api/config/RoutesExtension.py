# app/extensions
from app.presentation.rest_api.cities.CityProvinceAPI import city_blueprint


def register_routes(app):
    """ Register routes with blueprint and namespace """
    app.register_blueprint(city_blueprint)
