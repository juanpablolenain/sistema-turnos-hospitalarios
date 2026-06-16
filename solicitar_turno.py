from altas import registrar_paciente
from asignar_turno import mostrar_especialidades, obtener_especialidad, hay_disponibilidad, ocupar_turno

def solicitar_turno(pacientes):
    while True:
        dni = input("Ingrese DNI del paciente: ").strip()
        if dni in pacientes:
            print("Paciente: ", pacientes[dni]["nombre"])
            break
        else:
            print("No existe un paciente con el DNI: ", dni)
            print("1. Volver a intentar")
            print("2. Registrar paciente")
            opcion = int(input("Ingrese una opción: "))
            match opcion:
                case 1:
                    continue
                case 2:
                    registrar_paciente(pacientes)
                    return
    while True:
        mostrar_especialidades()
        opcion = input("Elija una opción: ")
        especialidad = obtener_especialidad(opcion)
        if especialidad is None:
            print("Opción inválida.")
            continue
        if hay_disponibilidad(especialidad):
            ocupar_turno(especialidad)
            print("Turno asignado correctamente.")
            break
        else:
            print("No hay turnos disponibles para", especialidad)