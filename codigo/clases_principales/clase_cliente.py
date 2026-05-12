from codigo.clases_principales.clase_base import ClaseBase
from codigo.excepciones.custom_errors import NombreVacioError, CorreoInvalidoError, TelefonoInvalidoError
# importamos las excepciones personalizadas para validar los datos del cliente y manejar errores de manera adecuada.

class Cliente(ClaseBase):
    # creamos sus propios atributos
    def __init__(self,id, nombre, correo,contacto):
        # llamamos al constructor de la clase base para inicializar los atributos heredados
        super().__init__(id, nombre) 
        self.correo = correo
        self.contacto = contacto
        self.validar_datos() 
    # --- validacion de datos----
    @property
    def correo(self):
        return self.__correo
    @property
    def contacto(self):
        return self.__contacto
    
    # --- setters para la validacion de datos----
    @correo.setter
    def correo(self, valor):
        if "@" not in valor or "." not in valor:
            raise CorreoInvalidoError(f"Formato de correo inválido: {valor}")
        self.__correo = valor
        
  
    @contacto.setter
    def contacto(self, valor):
        if not str(valor).isdigit() or len(str(valor)) < 7:
            raise TelefonoInvalidoError(f"Contacto no valido: {valor}")
        self.__contacto = valor
    
    # --- validacion general de datos----

    def validar_datos(self):
        # validacion nombre
        if not self.nombre or not self.nombre.strip():
            raise NombreVacioError("El nombre del cliente no puede estar vacío.")
        

    def mostrar_informacion(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Correo: {self.correo}, Contacto: {self.contacto}"
        
        

