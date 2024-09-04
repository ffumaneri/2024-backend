from typing import List, Optional, Union

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

app = FastAPI()

## DB
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

class ContactoBd(ORMBase): 
    __tablename__ = 'contactos'
    id = Column(Integer, primary_key=True) 
    nombre = Column(String(80), nullable=False)
    direccion = Column(String(120))
    telefonos = Column(String(50))

db_instance.create_all()

## FastAPI
class ContactoSinId(BaseModel): 
    nombre: str
    direccion: Optional[str]
    telefonos: Optional[str]

class Contacto(ContactoSinId): 
    id: int

@app.get("/contactos")
def getAllContacts(db: Session = Depends(db_instance.get_db)):
   return db.query(ContactoBd).all()

@app.get("/contactos/{id}")
def getContactoPorId(id: int, db: Session = Depends(db_instance.get_db)):
    cto = db.get(ContactoBd, id)
    if not cto:
        raise HTTPException(400, detail="id no encontrado")
    
    return cto

@app.get("/juanperez")
def getContactoPorNombre(db: Session = Depends(db_instance.get_db)):
    cto = db.query(ContactoBd).filter_by(nombre="juan perez").first()

    if not cto:
        raise HTTPException(400, detail="id no encontrado")
    
    return cto

@app.post("/contacto")
def addContact(c: ContactoSinId, db: Session = Depends(db_instance.get_db)):
    contacto_db =  ContactoBd()
    contacto_db.nombre = c.nombre
    contacto_db.direccion = c.direccion
    contacto_db.telefonos = c.telefonos

    db.add(contacto_db)
    db.commit()
    return {"code": "funciona"}

@app.delete("/contactos/{id}")
def deleteContacto(id: int, db: Session = Depends(db_instance.get_db)):
    cto = db.get(ContactoBd, id)
    if not cto:
        raise HTTPException(400, detail="id no encontrado")
    
    db.delete(cto)
    db.commit()
    return {"code": "funciona"}
