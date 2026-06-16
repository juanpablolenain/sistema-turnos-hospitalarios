from altas import registrar_paciente
from asignar_turno import mostrar_especialidades, obtener_especialidad, hay_disponibilidad, ocupar_turno, mostrar_prioridades, asignar_prioridad

def solicitar_turno(pacientes,  turnos, especialidades):
    while True:
        dni = input("Ingrese DNI del paciente: ").strip()
        if dni in pacientes:
            print("Paciente: ", pacientes[dni]["nombre"])
            break
        else:
            print("No existe un paciente con el DNI: ", dni)
            print("1. Volver a intentar")
            print("2. Registrar paciente")
            try:
                opcion = int(input("Ingrese una opción: "))
            except ValueError:
                print("Por favor ingrese un número.")
                continue
            match opcion:
                case 1:
                    continue
                case 2:
                    registrar_paciente(pacientes)
                    continue
    while True:
        mostrar_especialidades()
        opcion = input("Elija una opción: ")
        especialidad = obtener_especialidad(opcion)
        if especialidad is None:
            print("Opción inválida. Intente de nuevo")
            continue
        if hay_disponibilidad(especialidad, especialidades):
            mostrar_prioridades()
            opcion = input("Asigne una prioridad al paciente: ")
            prioridad = asignar_prioridad(opcion)
            if prioridad is None:
                print("Opción inválida. Intente de nuevo")
                continue
            ocupar_turno(especialidad, dni, prioridad, especialidades, turnos)
            print("Turno asignado correctamente.")
            break
        else:
            print("No hay turnos disponibles para", especialidad)