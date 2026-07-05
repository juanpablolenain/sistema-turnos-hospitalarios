from asignar_turno import mostrar_especialidades, obtener_especialidad
from atender_turno import ORDEN_PRIORIDAD


def obtener_turnos_pendientes(turnos, especialidad=None):
    pendientes = []
    for turno in turnos:
        if turno["estado"] == "pendiente":
            if especialidad is None or turno["especialidad"] == especialidad:
                pendientes.append(turno)
    pendientes.sort(
        key=lambda t: (
            t["especialidad"],
            ORDEN_PRIORIDAD[t["prioridad"]],
            t["id_turno"]
        )
    )
    return pendientes


def mostrar_turno(turno, pacientes):
    dni = turno["dni"]
    paciente = pacientes.get(dni, {})
    nombre = paciente.get("nombre", "Paciente no encontrado")
    obra_social = paciente.get("obra_social", "Sin dato")
    print(f"Turno #{turno['id_turno']}")
    print(f"  Paciente: {nombre}")
    print(f"  DNI: {dni}")
    print(f"  Obra social: {obra_social}")
    print(f"  Especialidad: {turno['especialidad']}")
    print(f"  Prioridad: {turno['prioridad']}")
    print(f"  Estado: {turno['estado']}")
    print("-" * 40)


def ver_turnos_pendientes(turnos, pacientes):
    print("\n--- Turnos pendientes ---")
    if not turnos:
        print("No hay turnos registrados en el sistema.")
        return
    print("1. Ver todos los turnos pendientes")
    print("2. Ver turnos pendientes por especialidad")
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor ingrese un número.")
            continue
        match opcion:
            case 1:
                pendientes = obtener_turnos_pendientes(turnos)
                break
            case 2:
                mostrar_especialidades()
                opcion_especialidad = input("Seleccione especialidad: ")
                especialidad = obtener_especialidad(opcion_especialidad)
                if especialidad is None:
                    print("Opción inválida. Intente de nuevo.")
                    continue
                pendientes = obtener_turnos_pendientes(turnos, especialidad)
                break
            case _:
                print("Opción inválida.")
    if not pendientes:
        print("No hay turnos pendientes para mostrar.")
        return
    print(f"\nCantidad de turnos pendientes: {len(pendientes)}")
    print("-" * 40)
    for turno in pendientes:
        mostrar_turno(turno, pacientes)