# ROOT_Project

from flask import Flask

from BaseConfig import BaseConfig
from app.infrastructure.persistence import initialize_sql
from app.presentation.rest_api.config.RoutesExtension import register_routes
from app.presentation.rest_api.config.ExceptionExtension import register_exception_handler


def create_app():
    app = Flask(__name__)
    app.config.from_object(BaseConfig)

    register_routes(app)
    register_exception_handler(app)

    return app
