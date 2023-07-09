"""
    Base class for all models
"""

from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session
from sqlalchemy import create_engine
from BaseConfig import config


class BaseModel(DeclarativeBase):
    """
        Base class for all models
    """
    
    engine = create_engine(config.DB_URI)
    session = scoped_session(sessionmaker(bind=engine))