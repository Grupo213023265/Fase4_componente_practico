# desarrollo de la clase de servicios 
# vamos a utilizar metodos astractos para cada servicio calculando su costo de forma diferente 
# importamos herramientas o librerias para desarrollar clases abtractas utilizando ABC 
# impotamos la clase base para heredar las librerias 
from codigo.clases_principales.clase_base import ClaseBase 

# from para importar la libreria ABC
from abc import ABC, abstractmethod 

# creamos la clase abstracta que representa todos los servicios de la compañia FJ
class Servicio (ClaseBase,ABC):
       
# definimos los atributos principales de cualquier servicio y sus espicificaciones 
    def __init__(self, id, nombre, precio_base, disponible=True): 
        super().__init__(id, nombre)
        # protegemos los atributos para que no sean modificables fuera de la clase 
        self._precio_base = precio_base
        self._disponible = disponible
        
# codigo para ontener el precio del servicio utilizando property
    @property
    def precio_base(self):
        return self._precio_base
    
# metodo para saber si esta disponible el servicio utilizando property
    @property
    def esta_disponible(self):
        # direccionando true si esta y false si no esta 
         return self._disponible 
     
# metodo para cambiar si no hay disponibilidad 
    def cambiar_disponibilidad(self, estado):
         self._disponible = estado
   
# cada servicio calculara su costo de manera diferente por eso
# utilizamos el metodo abstracto y se sobrepone sobre las clases hijas  
    @abstractmethod
    def calcular_costo(self):
            pass

# metodo abstracto para descrbir el servicio disponible ya que cada servicio
# ofrece una informacion distinta 
    @abstractmethod
    def describir_servicio(self):
         pass
   
# metodo abstracto para validar el serivio antes de usar el mismo
    @abstractmethod
    def validar_servicio(self):
        pass

# ciere de la clase abstracta servicios.

    
