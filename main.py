from altas import registrar_paciente
from solicitar_turno import solicitar_turno
from asignar_turno import especialidades

pacientes = {}
turnos = []


def mostrar_menu():
    print("\n--- SISTEMA DE TURNOS HOSPITALARIOS ---")
    print("1. Registrar paciente")
    print("2. Pedir un turno")
    print("3. Salir")


def main():
    opcion = ""
    while opcion != "3":
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))
        match opcion:
            case 1:
                registrar_paciente(pacientes)
            case 2:
                solicitar_turno(pacientes)
            case 3:
                print("Saliendo del sistema...")
            case _:
                print("Opción inválida.")
    print(especialidades)
    print(pacientes)
main()

