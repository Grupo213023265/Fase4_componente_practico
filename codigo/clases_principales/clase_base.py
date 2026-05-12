from abc import ABC, abstractmethod
# clase abstracta que sirve como base para las clases de cliente, reserva  y servicio

class ClaseBase(ABC):
    def __init__(self, id,nombre):
        self._id=id
        self._nombre=nombre
    
    @property
    def id(self): return self._id
        
    @property
    def nombre(self): return self._nombre
    
    # metodos abstractos que deben ser implementados por las clases cliente, reserva y servicio.
    @abstractmethod
    def mostrar_informacion(self):
        pass 
    
    @abstractmethod
    def validar_datos(self):
        pass
    
    
    
    
    