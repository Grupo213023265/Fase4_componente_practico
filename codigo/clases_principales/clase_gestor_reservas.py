from codigo.excepciones.custom_errors import ValidationError

class GestorReservas:
    def __init__(self):
        # Lista privada que actuará como nuestra base de datos en memoria
        self.__lista_reservas = []

    def agregar_reserva(self, reserva):
    #    Este método se encarga de validar y agregar una reserva al sistema
        try:
            # Primero ejecutamos la lógica de procesamiento de la reserva
            # que ya incluye las validaciones de cliente y servicio
            resultado = reserva.procesar_reserva()
            
            # Si no hubo errores, la añadimos a nuestra lista
            self.__lista_reservas.append(reserva)
            return f"Éxito: {resultado}"
            
        except ValidationError as e:
            # Re-lanzamos para que el main lo capture
            raise e

    def listar_reservas(self):
        """Devuelve una cadena con todas las reservas actuales."""
        if not self.__lista_reservas:
            return "No hay reservas registradas en el sistema."
        
        cuerpo = "=== LISTADO GENERAL DE RESERVAS ===\n"
        for r in self.__lista_reservas:
            cuerpo += r.mostrar_informacion() + "\n" + ("-" * 30) + "\n"
        return cuerpo

    def buscar_por_id(self, id_busqueda):
        """Busca una reserva específica por su ID."""
        for r in self.__lista_reservas:
            if r.id == id_busqueda:
                return r.mostrar_informacion()
        return f"No se encontró ninguna reserva con el ID: {id_busqueda}"

    def calcular_ingresos_totales(self):
        """Suma el costo de todas las reservas confirmadas."""
        total = sum(r.servicio.calcular_costo() for r in self._GestorReservas__lista_reservas if  r.estado == "Confirmada")
        return f"Ingresos totales del sistema: ${total}"