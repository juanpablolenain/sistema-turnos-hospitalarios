from altas import registrar_paciente
from solicitar_turno import solicitar_turno
pacientes = {}
turnos = []
especialidades = {
    "Clinica medica": {
        "cupo_maximo": 5,
        "turnos_asignados": 0
    },
    "Pediatria": {
        "cupo_maximo": 4,
        "turnos_asignados": 0
    },
    "Traumatologia": {
        "cupo_maximo": 3,
        "turnos_asignados": 0
    },
    "Cardiologia": {
        "cupo_maximo": 1,
        "turnos_asignados": 0
    },
    "Guardia": {
        "cupo_maximo": 10,
        "turnos_asignados": 0
    }
}


def mostrar_menu():
    print("\n--- SISTEMA DE TURNOS HOSPITALARIOS ---")
    print("1. Registrar paciente")
    print("2. Pedir un turno")
    print("4. Ver turnos pendientes")
    print("5. Atender siguiente turno")
    print("6. Ver estadísticas")
    print("7. Salir")


def main():
    opcion = ""
    while opcion != 7:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor ingrese un número.")
            continue
        match opcion:
            case 1:
                registrar_paciente(pacientes)
            case 2:
                solicitar_turno(pacientes, turnos, especialidades)
            case 3:
                print("Saliendo del sistema...")
            case _:
                print("Opción inválida.")
    print(turnos)
main()

