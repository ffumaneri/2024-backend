## DB
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# String de conexión a la base de datos
# postgresql+psycopg2://<user>:<password>@<host>:<puerto>/<nombre_base_de_datos>
SQLALCHEMY_DB_URL = "postgresql+psycopg2://admin_inspirecare:c7gFZCZqkbhAotttY473bW2GaR7Y6pqw@localhost:55432/utn"
"""
Database
clase para la conexión a la base de datos
"""
class Database():
    """
    Constructor
    """
    def __init__(self, connection_string: str = SQLALCHEMY_DB_URL, echo: bool = True):
        self.engine = create_engine(connection_string, echo=echo)
  
    """
    Obtiene la session local a través de sessionmaker
    """
    @property
    def SessionLocal(self):
        return sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    """
    Devuelve la session local para acceso a la base de datos.
    Es un generador: https://ellibrodepython.com/yield-python
    """
    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    """
    Crea las tables en base al modelo definido
    """
    def create_all(self):
        ORMBase.metadata.create_all(self.engine)
        
    """
    Borra las tablas creadas en base al modelo definido
    """
    def drop_all(self): 
        ORMBase.metadata.drop_all(bind=self.engine)

# Se crea un objeto para las clases bases del modelo
# esto quiere decir que todas las clases del modelo deben heredar de esta clase
ORMBase = declarative_base()

# Variable global para la instancia de la base de datos
db_instance = Database()