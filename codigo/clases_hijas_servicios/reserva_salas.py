from codigo.clases_principales.clase_servicio import Servicio
from codigo.excepciones.custom_errors import ValidationError

class ReservaSala(Servicio):
    def __init__(self, id, nombre, precio_base, capacidad, horas_reserva):
        super().__init__(id, nombre, precio_base)
        self.capacidad = capacidad
        self.horas_reserva = horas_reserva

    @property
    def capacidad(self): return self.__capacidad

    @capacidad.setter
    def capacidad(self, valor):
        if valor <= 0:
            raise ValidationError("La capacidad de la sala debe ser mayor a cero.")
        self.__capacidad = valor

    @property
    def horas_reserva(self): return self.__horas_reserva

    @horas_reserva.setter
    def horas_reserva(self, valor):
        if valor <= 0:
            raise ValidationError("Las horas de reserva deben ser mayores a cero.")
        self.__horas_reserva = valor

    def calcular_costo(self):
        return self.precio_base * self.horas_reserva

    def mostrar_informacion(self):
        return f"Sala: {self.nombre} (Capacidad: {self.capacidad} personas, {self.horas_reserva}h)."

    def validar_datos(self):
        return True