# from codigo.clases_hijas_servicios.alquiler_equipos import ServicioEquipo
# from codigo.clases_hijas_servicios.asesorias import Asesoria
# from codigo.clases_hijas_servicios.reserva_salas import ReservaSala
# from codigo.excepciones.custom_errors import ValidationError  , softwareFJError

# def ejecutar_pruebas_servicios():
#     print("--- INICIANDO PRUEBAS DE SERVICIOS ---")
    
#     try:
#         # 1. Prueba de Alquiler de Equipo (Caso Exitoso)
#         laptop = ServicioEquipo(101, "MacBook Pro", 50.0, "Computador Portátil")
#         print(f"Éxito: {laptop.mostrar_informacion()}")
#         print(f"Costo por 3 días: ${laptop.calcular_costo(3)}")

#         # 2. Prueba de Asesoría (Caso con Error: Horas negativas)
#         print("\nIntentando crear asesoría con horas inválidas...")
#         asesoria_pro = Asesoria(201, "Consultoría Java", 100.0, -2, "Ing. Juan Pérez")
        
#     except ValidationError as e:
#         print(f"Validación detectada: {e}")
#     except softwareFJError as e:
#         print(f"Error general del sistema: {e}")
#     except Exception as e:
#         print(f"Error inesperado: {e}")

#     try:
#         # 3. Prueba de Reserva de Sala (Caso Exitoso)
#         sala_juntas = ReservaSala(301, "Sala A", 30.0, 10, 4)
#         if sala_juntas.validar_datos():
#             print(f"\nÉxito: {sala_juntas.mostrar_informacion()}")
#             print(f"Total Reserva: ${sala_juntas.calcular_costo()}")
            
#     except ValidationError as e:
#         print(f"Error en Sala: {e}")

# if __name__ == "__main__":
#         ejecutar_pruebas_servicios()

from codigo.clases_principales.clase_cliente import Cliente
from codigo.excepciones.custom_errors import softwareFJError

clientes_prueba = [
    (1, "Samuel Mora", "samuel@gmail.com", "3124567890"),
    (2, "", "juan@gmail.com", "3001234567"), # Error Nombre
    (3, "Laura", "lauragmail.com", "3014567890") # Error Correo
]

for id_e, nom, corr, tel in clientes_prueba:
    try:
        c = Cliente(id_e, nom, corr, tel)
        c.mostrar_informacion()
    except softwareFJError as e: # Atrapa cualquiera de nuestras 3 excepciones
        print(f"¡ALERTA!: {e}")
    finally:
        print("--- Fin de registro ---")