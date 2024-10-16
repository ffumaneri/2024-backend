"""
repository.py
"""
from model import ContactoBd, DireccionDb

"""
Clase que hereda de Exception. Indica que no se encontró un recurso solicitado.
"""
class NotFoundError(Exception):

    def __init__(self, message):
        super().__init__(message)
        self._status_code = 404

    @property
    def status_code(self):
        # Codigo de estado (solo lectura)
        return self._status_code
    
"""
Clase que hace las consultas necesarias a la base de datos.
"""
class ContactosRepo:
    def getAll(self, db):
        # Este método devuelve un arreglo de Tuplas.
        #[(ContactoDb, DireccionDb)]
        # 
        filas = db.query(ContactoBd, DireccionDb).join(DireccionDb).all()
        objetos = []
        for fila in filas:
            contacto, direccion = fila
            objetos.append({"nombre": contacto.nombre, "telefonos": contacto.telefonos, "calle": direccion.calle, "numero": direccion.numero})

        return objetos
    
    def getOne(self, id, db):
        cto = db.get(ContactoBd, id)
        if not cto:
            raise NotFoundError("id no encontrado")
        
        return cto
    
    def searchByName(self, nombre, db):
        cto = db.query(ContactoBd).filter_by(nombre=nombre).first()

        if not cto:
            raise NotFoundError("id no encontrado")
        
        return cto
    
    def add(self, contacto_db, db):
        db.add(contacto_db)
        db.commit()

    def delete(self, id, db):
        cto = self.getOne(id, db)
        db.delete(cto)
        db.commit()

