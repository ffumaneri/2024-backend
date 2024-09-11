from model import ContactoBd

"""
Indica que no se encontró un recurso solicitado.
"""
class NotFoundError(Exception):

    def __init__(self, message):
        super().__init__(message)
        self._status_code = 404

    @property
    def status_code(self):
        # Codigo de estado (solo lectura)
        return self._status_code
    
class ContactosRepo:
    def getAll(self, db):
        return db.query(ContactoBd).all()
    
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

