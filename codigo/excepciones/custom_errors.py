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

Class softwareFJError(Exception):
    def __init__(self,mensaje):
        super().__init__(mensaje)
        logging.error(f"{self.__class__.__name__}: {mensaje}")

# CLASES PARA LAS EXCEPCIONES PERSONALIZADAS

class NombreVacioError(SoftwareFJError):
    pass

class CorreoInvalidoError(SoftwareFJError):
    pass

class TelefonoInvalidoError(SoftwareFJError):
    pass
