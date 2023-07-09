# app/extensions
from app.presentation.rest_api.cities.CityAPI import city_api


def register_routes(app):
    """ Register routes with blueprint and namespace """
    app.register_blueprint(city_api, url_prefix='/api/v1/')
