
# importamos la clase abstracta Servicio
from codigo.clases_principales.clase_servicio import Servicio

# importamos la excepcion personalizada
from codigo.excepciones.custom_errors import ValidationError


# clase hija ReservaSala que hereda de Servicio
class ReservaSala(Servicio):

    # constructor de la clase
    def __init__(
        self,
        id,
        nombre,
        precio_base,
        capacidad,
        horas_reserva
    ):

        # heredamos atributos de la clase padre
        super().__init__(id, nombre, precio_base)

        # atributos propios de la reserva de sala
        self.capacidad = capacidad
        self.horas_reserva = horas_reserva

    # metodo sobrescrito para calcular el costo
    def calcular_costo(self):

        # calculamos el costo dependiendo de las horas
        return self._precio_base * self.horas_reserva

    # metodo sobrescrito para describir el servicio
    def describir_servicio(self):

        return (
            f"Sala con capacidad para "
            f"{self.capacidad} personas "
            f"reservada por "
            f"{self.horas_reserva} horas"
        )

    # metodo sobrescrito para validar el servicio
    def validar_servicio(self):

        # validacion de capacidad
        if self.capacidad <= 0:
            raise ValidationError(
                f"La capacidad de la sala debe ser mayor a cero."
            )

        # validacion de horas de reserva
        if self.horas_reserva <= 0:
            raise ValidationError(
                f"Las horas de reserva deben ser mayores a cero."
            )

        return True
