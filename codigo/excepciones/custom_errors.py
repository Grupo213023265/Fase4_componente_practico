import logging
import os

# =========================
# CONFIGURACIÓN DEL LOG
# =========================
# creamos la carpeta de logs existentes
os.makedirs("codigo/archivo_de_errores", exist_ok=True)

logging.basicConfig(
    filename="sistema.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =========================
# CLASE BASE PARA LAS EXCEPCIONES
# =========================

class softwareFJError(Exception):
    def __init__(self,mensaje):
        super().__init__(mensaje)
        logging.error(f"{self.__class__.__name__}: {mensaje}")

# CLASES PARA LAS EXCEPCIONES PERSONALIZADAS

class NombreVacioError(softwareFJError):
    pass

class CorreoInvalidoError(softwareFJError):
    pass

class TelefonoInvalidoError(softwareFJError):
    pass
