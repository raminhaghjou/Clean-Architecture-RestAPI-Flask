
from app.infrastructure.persistence import initialize_sql
from sqlalchemy import create_engine

from app.presentation.rest_api.config.BaseConfig import BaseConfig as app_config

engine = create_engine(app_config.DB_URI)
initialize_sql(engine)
