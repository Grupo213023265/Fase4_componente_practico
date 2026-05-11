from codigo.clases_principales.clase_base import ClaseBase
# la clase cliente hereda de la clase base.
class Cliente(ClaseBase):
    # creamos sus propios atributos
    def __init__(self,id, nombre, correo,contacto):
        # llamamos al constructor de la clase base para inicializar los atributos heredados
        super().__init__(id, nombre) 
        self.__correo = correo
        self.__contacto = contacto
        
    #creamos decoradores properties y setters para validar datos.
    # ----Validacion de correo----
    @property
    def correo(self):
        return self.__correo
    @correo.setter
    def correo(self, valor):
        if "@" not in valor or "." not in valor:
            # ----Excepción correo no válido----
            raise ValueError(f"Correo no valido: {valor}")
        self.__correo = valor
    # ----Validacion de contacto----
    @property
    def contacto(self):
        return self.__contacto
    @contacto.setter
    def contacto(self, valor):
        if not str(valor).isdigit() or len(str(valor)) < 7:
            # ----Excepción contacto no válido----
            raise ValueError(f"Contacto no valido: {valor}")
        self.__contacto = valor
    
    def validar_datos(self):
        pass
    
    def mostrar_informacion(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Correo: {self.correo}, Contacto: {self.contacto}"
        
        

