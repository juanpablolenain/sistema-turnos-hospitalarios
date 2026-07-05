from altas import registrar_paciente
from solicitar_turno import solicitar_turno
from atender_turno import atender_turno
from estadisticas import ver_estadisticas
from ver_turnos import ver_turnos_pendientes

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
        "cupo_maximo": 3,
        "turnos_asignados": 0
    }
}

def mostrar_menu():
    print("\n--- SISTEMA DE TURNOS HOSPITALARIOS ---")
    print("1. Registrar paciente")
    print("2. Pedir un turno")
    print("3. Ver turnos pendientes")
    print("4. Atender siguiente turno")
    print("5. Ver estadísticas")
    print("6. Salir")

def main():
    opcion = ""
    while opcion != 6:
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
                ver_turnos_pendientes(turnos, pacientes)
            case 4:
                atender_turno(turnos, pacientes, especialidades)
            case 5:
                ver_estadisticas(turnos, especialidades, pacientes)
            case 6:
                print("Saliendo del sistema...")
            case _:
                print("Opción inválida.")
main()
