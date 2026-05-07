from abc import ABC, abstractmethod

class ClaseBase(ABC):
    def __init__(self, id,nombre):
        self.id=id
        self.nombre=nombre
    
    @property
    def id(self): return self._id
    
    @property
    def nombre(self): return self._nombre
    
    @abstractmethod
    def mostrar_informacion(self):
        pass
    
    @abstractmethod
    def validar_datos(self):
        pass
    
    
    
    
    