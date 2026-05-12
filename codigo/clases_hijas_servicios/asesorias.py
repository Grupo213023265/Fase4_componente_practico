<<<<<<< HEAD
=======

>>>>>>> 200ba580f7429893e515e0e69c533ae205550e02

# importamos la clase abstracta Servicio
from codigo.clases_principales.clase_servicio import Servicio

# importamos la excepcion personalizada
from codigo.excepciones.custom_errors import ValidationError


# clase hija Asesoria que hereda de Servicio
class Asesoria(Servicio):

    # constructor de la clase
    def __init__(self, id, nombre, precio_base, horas, especialista):

        # heredamos atributos de la clase padre
        super().__init__(id, nombre, precio_base)

        # atributos propios de la asesoria
        self.horas = horas
        self.especialista = especialista

    # metodo sobrescrito para calcular el costo
    def calcular_costo(self):

        # calculamos el costo dependiendo de las horas
        return self._precio_base * self.horas

    # metodo sobrescrito para describir el servicio
    def describir_servicio(self):

        return (
            f"Asesoría especializada con "
            f"{self.especialista} "
            f"durante {self.horas} horas"
        )

    # metodo sobrescrito para validar el servicio
    def validar_servicio(self):

        # validacion de horas
        if self.horas <= 0:
            raise ValidationError(
                f"Las horas de asesoría deben de ser mayores a cero."
            )

        # validacion del especialista
        if not self.especialista.strip():
            raise ValidationError(
                f"Debe asignarse un especialista válido."
            )

        return True
