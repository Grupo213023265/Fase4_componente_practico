# importamos las clases necesarias para la construccion de esta clase hija de servicios
from codigo.clases_principales.clase_servicio import Servicio
from codigo.excepciones.custom_errors import ValidationError

# definir la clase hija ServicioEquipo que hereda de Servicio y ClaseBase 
class ServicioEquipo(Servicio):
    
    # Construimos la clase 
    def __init__(self, id, nombre, precio_base, tipo_equipo, disponible=True):
        
        # llamamos al constructor de la clase padre 
        super().__init__(id, nombre, precio_base, disponible)
        
        # los atributos propios de la clase como tipo de quipo, computador y demas
        self._tipo_equipo = tipo_equipo
        
    #vamos a calcular el costo del servicio considerando el tiempo de alquiler 
    def calcular_costo(self, dias=1):
    
        # validamos que los dias sean correctos
        if dias <= 0:
            raise ValidationError("los dias deben ser mayores a 0")
             
        # multiplicamos el precio base por los dias 
        return self._precio_base * dias
    
    # descripcion del servicio
    def mostrar_informacion(self):
        
        #descripcion del servicio 
        return f"alquiler de equipo tipo: {self._tipo_equipo}"
    
    # validamos el servicio antes de su uso 
    def validar_datos(self):
        
        # Validar que el equipo no este vacio 
        if not self._tipo_equipo:
            raise ValidationError("el tipo de equipo no puede estar vacio")
            
        # validamos que el precio sea valido
        if self._precio_base <= 0:
            raise ValidationError("el precio base debe ser mayor a 0")
            
        # si todo esta bien retorna a verdadero
        return True
            
            
            