## DB
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DB_URL = "postgresql+psycopg2://admin_inspirecare:c7gFZCZqkbhAotttY473bW2GaR7Y6pqw@localhost:55432/utn"

class Database():
    def __init__(self, connection_string: str = SQLALCHEMY_DB_URL, echo: bool = True):
        self.engine = create_engine(connection_string, echo=echo)
    @property
    def SessionLocal(self):
        return sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def create_all(self):
        ORMBase.metadata.create_all(bind=self.engine)
        
    def drop_all(self): 
        ORMBase.metadata.drop_all(bind=self.engine)

db_instance = Database()
ORMBase = declarative_base()
