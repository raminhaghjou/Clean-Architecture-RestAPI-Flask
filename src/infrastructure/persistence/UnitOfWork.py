from contextlib import contextmanager
from src.core.services.infra.UnitOfWorkBase import UnitOfWorkBase
from src.infrastructure.persistence import DBSession

# Define the unit of work class
class UnitOfWork(UnitOfWorkBase):
    def __init__(self, session: DBSession):
        self.session = session
    
    def begin(self):
        return self.session.begin()
    
    def rollback(self):
        return self.session.rollback()
        
    def commit(self):
        return self.session.commit()
