# """
#     Base class for all models
# """

# from sqlalchemy.orm import sessionmaker, scoped_session
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine
# from BaseConfig import BaseConfig as config

# base = declarative_base()
# class BaseModel(base):
#     """
#         Base class for all models
#     """
    
# engine = create_engine(config.DB_URI)
# session = scoped_session(sessionmaker(bind=engine))