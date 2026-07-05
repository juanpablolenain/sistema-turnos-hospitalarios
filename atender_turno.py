ORDEN_PRIORIDAD = {"Alta": 0, "Media": 1, "Baja": 2}


def obtener_siguiente_turno(especialidad, turnos):
    pendientes = [
        t for t in turnos
        if t["especialidad"] == especialidad and t["estado"] == "pendiente"
    ]
    if not pendientes:
        return None
    pendientes.sort(key=lambda t: (ORDEN_PRIORIDAD[t["prioridad"]], t["id_turno"]))
    return pendientes[0]


def mostrar_siguiente_turno(turno, pacientes):
    paciente = pacientes[turno["dni"]]
    print(f"\nSiguiente turno en atención:")
    print(f"  Turno #{turno['id_turno']}  ·  {paciente['nombre']}  ·  Prioridad: {turno['prioridad']}")


def seleccionar_nuevo_estado():
    print("\n¿Qué pasó con este paciente?")
    print("1. Atendido")
    print("2. Ausente")
    print("3. Cancelado")
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor ingrese un número.")
            continue
        match opcion:
            case 1:
                return "atendido"
            case 2:
                return "ausente"
            case 3:
                return "cancelado"
            case _:
                print("Opción inválida.")