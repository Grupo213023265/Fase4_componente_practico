from abc import ABC, abstractmethod
# clase abstracta que sirve como base para las clases de cliente, reserva  y servicio

class ClaseBase(ABC):
    def __init__(self, id,nombre):
        self.id=id
        self.nombre=nombre
    
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
    
        
    from abc import ABC, abstractmethod
from datetime import date

class Reserva(ABC):
    def __init__(self, cliente, servicio, fecha):
        if cliente is None:
            raise ValueError("El cliente no puede ser nulo")
        if servicio is None:
            raise ValueError("El servicio no puede ser nulo")
        if fecha < date.today():
            raise ValueError("La fecha de reserva no puede ser pasada")

        self._cliente = cliente
        self._servicio = servicio
        self._fecha = fecha
        self._activa = True

    # Encapsulación con propiedades
    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def fecha(self):
        return self._fecha

    @property
    def activa(self):
        return self._activa

    # Método para cancelar la reserva
    def cancelar(self):
        self._activa = False

    # Método abstracto (cada tipo de reserva define su costo)
    @abstractmethod
    def calcular_costo(self):
        pass

    def __str__(self):
        estado = "Activa" if self._activa else "Cancelada"
        return f"Reserva de {self._cliente} para {self._servicio} en {self._fecha} | Estado: {estado}"

    
    
    