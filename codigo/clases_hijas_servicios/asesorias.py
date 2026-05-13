#inportamos la clase Servicio y la clase ValidationError para poder usar sus funcionalidades en esta clase hija
from codigo.clases_principales.clase_servicio import Servicio
from codigo.excepciones.custom_errors import ValidationError

class Asesoria(Servicio):
    def __init__(self, id, nombre, precio_base, horas, especialista):
        super().__init__(id, nombre, precio_base)
        self.horas = horas
        self.especialista = especialista

    @property
    def horas(self): return self.__horas

    @horas.setter
    def horas(self, valor):
        if valor <= 0:
            raise ValidationError("Las horas de asesoría deben ser mayores a cero.")
        self.__horas = valor

    @property
    def especialista(self): return self.__especialista

    @especialista.setter
    def especialista(self, valor):
        if not valor or not valor.strip():
            raise ValidationError("Debe asignarse un especialista válido.")
        self.__especialista = valor

    def calcular_costo(self):
        return self.precio_base * self.horas

    def describir_servicio(self):
        return f"Asesoría: {self.nombre} con {self.especialista} ({self.horas} horas)."

    def validar_servicio(self):
        
        return True
