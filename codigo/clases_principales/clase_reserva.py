# antes de ejecutar el proyecto debe actualizar el repositorio
# para evitar errores con las nuevas excepciones personalizadas

# importamos las excepciones personalizadas
from codigo.excepciones.custom_errors import (
    ValidationError,
    ProcessingError
)


# clase Reserva
class Reserva:

    # constructor de la clase
    def __init__(
        self,
        id_reserva,
        cliente,
        servicio,
        duracion,
        estado="Pendiente"
    ):

        # atributos de la reserva
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = estado

    # metodo para confirmar la reserva
    def confirmar_reserva(self):

        try:

            # validacion del cliente
            if self.cliente is None:
                raise ValidationError(
                    f"Debe asignarse un cliente válido."
                )

            # validacion del servicio
            if self.servicio is None:
                raise ValidationError(
                    f"Debe asignarse un servicio válido."
                )

            # validamos el servicio
            self.servicio.validar_servicio()

            # verificamos disponibilidad
            if not self.servicio.esta_disponible:
                raise ValidationError(
                    f"El servicio no se encuentra disponible."
                )

            # validacion de duracion
            if self.duracion <= 0:
                raise ValidationError(
                    f"La duración de la reserva debe ser mayor a cero."
                )

            # cambiamos el estado
            self.estado = "Confirmada"

            return (
                f"Reserva confirmada correctamente."
            )

        except ValidationError as error:

            raise ProcessingError(
                f"Error al confirmar la reserva."
            ) from error

    # metodo para cancelar reserva
    def cancelar_reserva(self):

        try:

            # verificamos si ya esta cancelada
            if self.estado == "Cancelada":
                raise ValidationError(
                    f"La reserva ya se encuentra cancelada."
                )

            self.estado = "Cancelada"

            return (
                f"Reserva cancelada correctamente."
            )

        except ValidationError as error:

            raise ProcessingError(
                f"Error al cancelar la reserva."
            ) from error

    # metodo para procesar reserva
    def procesar_reserva(self):

        try:

            mensaje = self.confirmar_reserva()

            costo_total = (
                self.servicio.calcular_costo()
            )

            return (
                f"{mensaje}\n"
                f"Costo total: ${costo_total}"
            )

        except Exception as error:

            raise ProcessingError(
                f"Error procesando la reserva."
            ) from error

    # metodo para mostrar informacion
    def mostrar_reserva(self):

        return (
            f"\nID Reserva: {self.id_reserva}\n"
            f"Duración: {self.duracion}\n"
            f"Estado: {self.estado}"
        )
