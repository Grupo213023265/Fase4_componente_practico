from codigo.clases_principales.clase_base import ClaseBase
from codigo.excepciones.custom_errors import ValidationError 

# clase Reserva
class Reserva (ClaseBase):

    # constructor de la clase
    def __init__(
        self,
        id,
        nombre_reserva,
        cliente,
        servicio,
        duracion,
        estado="Pendiente"
    ):

        super().__init__(id, nombre_reserva)
    
        # atributos de la reserva
        
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = estado
        
    @property
    def servicio(self):
        return self.__servicio

    @property
    def estado(self):
        return self.__estado

    # metodo para validar los datos de la reserva
    def validar_datos(self):
        
            # validacion del cliente
        if self.__cliente is None:
            raise ValidationError(f"Debe asignarse un cliente válido.")
                

            # validacion del servicios
        if self.__servicio is None:
                raise ValidationError(
                    f"Debe asignarse un servicio válido."
                )
        if self.__duracion <= 0:
                raise ValidationError(
                    f"La duración de la reserva debe ser mayor a cero."
                )
        return True
    # metodo para confirmar reserva
    def mostrar_informacion(self):
         return  (

            f"Reserva: {self.nombre}\n"
            f"Nombre cliente: {self.__cliente.nombre}\n"
            f"Estado: {self.__estado}\n"
         )
         
         
    def confirmar_reserva(self):
            # verificamos disponibilidad
        if not self.__servicio.esta_disponible:
                raise ValidationError(
                    f"El servicio no se encuentra disponible."
                )
            # cambiamos el estado
        self.__estado = "Confirmada"
        return (
                f"Reserva confirmada correctamente."
            )
        
    def procesar_reserva(self):
        mensaje = self.confirmar_reserva()
        costo_total = self.__servicio.calcular_costo() 
        return f"{mensaje} Costo total: {costo_total}"