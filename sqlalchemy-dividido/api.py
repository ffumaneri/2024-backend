## FastAPI
from typing import Optional
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from db import db_instance
from model import ContactoBd
from repository import ContactosRepo, NotFoundError

app = FastAPI()
repo = ContactosRepo()
class ContactoSinId(BaseModel): 
    nombre: str
    direccion: Optional[str]
    telefonos: Optional[str]

class Contacto(ContactoSinId): 
    id: int

@app.get("/contactos")
def getAllContacts(db: Session = Depends(db_instance.get_db)):
   return repo.getAll(db)

@app.get("/contactos/{id}")
def getContactoPorId(id: int, db: Session = Depends(db_instance.get_db)):
    try:
        return repo.getOne(id, db)
    except NotFoundError as e:
        raise HTTPException(e.status_code, e.message)

@app.get("/search/{nombre}")
def getContactoPorNombre(nombre: str, db: Session = Depends(db_instance.get_db)):
    try:
        cto = repo.searchByName(nombre, db)
    except NotFoundError as e:
        raise HTTPException(e.status_code, "id no encontrado")
    
    return cto

@app.post("/contacto")
def addContact(c: ContactoSinId, db: Session = Depends(db_instance.get_db)):
    contacto_db =  ContactoBd()
    contacto_db.nombre = c.nombre
    contacto_db.direccion = c.direccion
    contacto_db.telefonos = c.telefonos

    repo.add(contacto_db, db)

    return {"code": "funciona"}

@app.delete("/contactos/{id}")
def deleteContacto(id: int, db: Session = Depends(db_instance.get_db)):
    try:
        cto = repo.getOne(id, db)
        db.delete(cto)
        db.commit()

    except NotFoundError as e:
        raise HTTPException(e.status_code, "id no encontrado")
    
    return {"code": "funciona"}
