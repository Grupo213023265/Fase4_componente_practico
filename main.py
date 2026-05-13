# inportamos las clases necesarias para ejecutar la prueba del sistema de gestión
from codigo.clases_principales.clase_cliente import Cliente
from codigo.clases_hijas_servicios.asesorias import Asesoria
from codigo.clases_hijas_servicios.alquiler_equipos import ServicioEquipo
from codigo.clases_hijas_servicios.reserva_salas import ReservaSala
from codigo.clases_principales.clase_gestor_reservas import GestorReservas
from codigo.clases_principales.clase_reserva import Reserva
from codigo.excepciones.custom_errors import ValidationError, softwareFJError

def main():
    sistema = GestorReservas()
    print("=== INICIANDO LAS 10 PRUEBAS TÉCNICAS - SOFTWARE FJ ===\n")

    # --- BLOQUE 1: CLIENTES ---
    print("1. Registro de Cliente Válido:")
    try:
        c1 = Cliente(1, "Deisy Agreda", "deisy@unad.edu.co", "3001234567")
        print(f"   [OK] Cliente creado: {c1.nombre}")
    except ValidationError as e: print(f"   [FALLO] {e}")

    print("\n2. Registro de Cliente Inválido (Email sin @):")
    try:
        c_error = Cliente(2, "Juan Perez", "juan_correo.com", "310")
        print("   [FALLO] El sistema permitió un correo inválido.")
    except Exception as e: 
        print(f"   [EXITO EN PRUEBA] Error capturado: {e}")

    # --- BLOQUE 2: SERVICIOS ---
    print("\n3. Creación Correcta de Servicio (Alquiler):")
    try:
        s1 = ServicioEquipo(101, "Laptop Dell", 45000.0, "Computador")
        print(f"   [OK] Servicio creado: {s1.nombre}")
    except Exception as e: print(f"   [FALLO] {e}")

    print("\n4. Creación Incorrecta de Servicio (Precio Negativo):")
    try:
        s_error = Asesoria(102, "Asesoría Java", -500.0, 2, "Ing. Gomez")
    except ValidationError as e: 
        print(f"   [EXITO EN PRUEBA] Error capturado: {e}")

    print("\n5. Creación Incorrecta de Servicio (Sin Especialista):")
    try:
        s_error2 = Asesoria(103, "Ciberseguridad", 80000.0, 1, "")
    except ValidationError as e: 
        print(f"   [EXITO EN PRUEBA] Error capturado: {e}")

    # --- BLOQUE 3: RESERVAS ---
    print("\n6. Reserva Exitosa (Asesoría):")
    try:
        c2 = Cliente(3, "Carlos Ruiz", "carlos@mail.com", "3204567890")
        s2 = Asesoria(201, "Consultoría Python", 120000.0, 2, "Dr. Arbey")
        r1 = Reserva(5001, "Reserva Mayo", c2, s2, 2)
        print(f"   {sistema.agregar_reserva(r1)}")
    except Exception as e: print(f"   [FALLO] {e}")

    print("\n7. Reserva Exitosa (Sala de Juntas):")
    try:
        s3 = ReservaSala(301, "Sala Creativa", 50000.0, 10, 4)
        r2 = Reserva(5002, "Reunión Equipo", c1, s3, 4)
        print(f"   {sistema.agregar_reserva(r2)}")
    except Exception as e: print(f"   [FALLO] {e}")

    print("\n8. Reserva Fallida (Servicio No Disponible):")
    try:
        s4 = ServicioEquipo(401, "Proyector", 30000.0, "Multimedia")
        s4.cambiar_disponibilidad(False) # Lo ponemos fuera de servicio
        r3 = Reserva(5003, "Préstamo Proyector", c1, s4, 1)
        sistema.agregar_reserva(r3)
    except ValidationError as e: 
        print(f"   [EXITO EN PRUEBA] Error capturado: {e}")

    print("\n9. Reserva Fallida (Duración en Cero):")
    try:
        r4 = Reserva(5004, "Reserva Error", c1, s1, 0)
        sistema.agregar_reserva(r4)
    except ValidationError as e: 
        print(f"   [EXITO EN PRUEBA] Error capturado: {e}")

    # --- BLOQUE 4: GESTIÓN TOTAL ---
    print("\n10. Informe Final del Gestor:")
    print(sistema.listar_reservas())
    print(sistema.calcular_ingresos_totales())

if __name__ == "__main__":
    main()
    
    