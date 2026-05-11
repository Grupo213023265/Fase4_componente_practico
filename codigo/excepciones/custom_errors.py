import logging

# =========================
# CONFIGURACIÓN DEL LOG
# =========================

logging.basicConfig(
    filename="sistema.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =========================
# EXCEPCIONES PERSONALIZADAS
# =========================

class NombreVacioError(Exception):
    pass

class CorreoInvalidoError(Exception):
    pass

class TelefonoInvalidoError(Exception):
    pass

# =========================
# CLASE CLIENTE
# =========================

class Cliente:

    def __init__(self, nombre, correo, telefono):

        # Validación nombre
        if not nombre.strip():
            raise NombreVacioError(
                "El nombre del cliente no puede estar vacío"
            )

        # Validación correo
        if "@" not in correo or "." not in correo:
            raise CorreoInvalidoError(
                "El correo ingresado no es válido"
            )

        # Validación teléfono
        if not telefono.isdigit():
            raise TelefonoInvalidoError(
                "El teléfono debe contener solo números"
            )

        # Encapsulación
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    # Métodos GET
    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def get_telefono(self):
        return self.__telefono

    # Mostrar información
    def mostrar_info(self):
        print("\nCLIENTE REGISTRADO")
        print(f"Nombre: {self.__nombre}")
        print(f"Correo: {self.__correo}")
        print(f"Teléfono: {self.__telefono}")
        # =========================
# PRUEBAS DEL SISTEMA
# =========================

clientes_prueba = [

    ("Samuel Mora", "samuel@gmail.com", "3124567890"),

    ("", "juan@gmail.com", "3001234567"),

    ("Laura", "lauragmail.com", "3014567890"),

    ("Carlos", "carlos@gmail.com", "telefono"),

    ("Ana", "ana@gmail.com", "3209876543")
]

print("===== SISTEMA DE CLIENTES =====")

for datos in clientes_prueba:

    try:

        cliente = Cliente(
            datos[0],
            datos[1],
            datos[2]
        )

    except NombreVacioError as e:

        print(f"\nERROR: {e}")

        logging.error(
            f"Error de nombre: {e}"
        )

    except CorreoInvalidoError as e:

        print(f"\nERROR: {e}")

        logging.error(
            f"Error de correo: {e}"
        )

    except TelefonoInvalidoError as e:

        print(f"\nERROR: {e}")

        logging.error(
            f"Error de teléfono: {e}"
        )

    except Exception as e:

        print(f"\nERROR GENERAL: {e}")

        logging.error(
            f"Error general: {e}"
        )

    else:

        cliente.mostrar_info()

    finally:

        print("Proceso finalizado.\n")

print("El sistema continúa funcionando correctamente.")