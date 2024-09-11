from sqlalchemy import Column, Integer, String
from db import ORMBase

class ContactoBd(ORMBase): 
    __tablename__ = 'contactos'
    id = Column(Integer, primary_key=True) 
    nombre = Column(String(80), nullable=False)
    direccion = Column(String(120))
    telefonos = Column(String(50))
