"""
model.py

en este archivo se declara el modelo de base de datos
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from db import ORMBase, db_instance
from sqlalchemy.orm import relationship


"""
ContactoDb
Clase python que define el mapeo con la tabla contactos
"""
class ContactoBd(ORMBase): 
    __tablename__ = 'contactos'
    id = Column(Integer, primary_key=True) 
    nombre = Column(String(80), nullable=False)
    telefonos = Column(String(50))
    direccion_id= Column(Integer, ForeignKey("direccion.id"))
    direccion = relationship("DireccionDb", foreign_keys=[direccion_id])

"""
DireccionDb
Clase python que define el mapeo con la tabla direccion
"""
class DireccionDb(ORMBase):
    __tablename__ = 'direccion'
    id = Column(Integer, primary_key=True)
    calle = Column(String(80), nullable=False)
    numero = Column(String(80), nullable=False)
    ciudad = Column(String(80), nullable=False)

db_instance.create_all()