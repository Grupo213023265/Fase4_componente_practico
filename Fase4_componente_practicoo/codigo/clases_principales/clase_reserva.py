## Parte de Reservas
En esta sección se implementa la clase `Reserva` y el `GestorReservas`, 
encargados de administrar la creación, listado y cancelación de reservas 

public class Reserva {
    private Cliente cliente;
    private Servicio servicio;
    private LocalDate fecha;
    private boolean activa;

    // Constructor con validaciones
    public Reserva(Cliente cliente, Servicio servicio, LocalDate fecha) throws Exception {
        if(cliente == null) throw new Exception("El cliente no puede ser nulo");
        if(servicio == null) throw new Exception("El servicio no puede ser nulo");
        if(fecha.isBefore(LocalDate.now())) throw new Exception("La fecha de reserva no puede ser pasada");

        this.cliente = cliente;
        this.servicio = servicio;
        this.fecha = fecha;
        this.activa = true;
    }

    // Getters
    public Cliente getCliente() { return cliente; }
    public Servicio getServicio() { return servicio; }
    public LocalDate getFecha() { return fecha; }
    public boolean isActiva() { return activa; }

    // Cancelar reserva
    public void cancelar() {
        this.activa = false;
    }

    // Mostrar información
    @Override
    public String toString() {
        return "Reserva de " + cliente.getNombre() +
               " para el servicio: " + servicio.getNombre() +
               " en la fecha: " + fecha +
               " | Estado: " + (activa ? "Activa" : "Cancelada");
    }
}

### Funcionalidades principales
- Crear reservas asociando clientes y servicios.
import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class GestorReservas {
    private List<Reserva> reservas = new ArrayList<>();

    // Crear nueva reserva
    public void crearReserva(Cliente cliente, Servicio servicio, LocalDate fecha) {
        try {
            Reserva nueva = new Reserva(cliente, servicio, fecha);
            if(reservas.contains(nueva)) {
                throw new Exception("La reserva ya existe");
            }
            reservas.add(nueva);
            System.out.println("Reserva creada exitosamente.");
        } catch (Exception e) {
            System.err.println("Error al crear reserva: " + e.getMessage());
        }
    }

    // Listar reservas
    public void listarReservas() {
        if(reservas.isEmpty()) {
            System.out.println("No hay reservas registradas.");
        } else {
            reservas.forEach(r -> System.out.println(r));
        }
    }

    // Cancelar reserva
    public void cancelarReserva(Reserva r) {
        if(reservas.contains(r)) {
            r.cancelar();
            System.out.println("Reserva cancelada.");
        } else {
            System.err.println("La reserva no existe.");
        }
    }
}
