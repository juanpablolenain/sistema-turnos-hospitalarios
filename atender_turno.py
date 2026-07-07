ORDEN_PRIORIDAD = {"Alta": 0, "Media": 1, "Baja": 2}

def atender_turno(turnos, pacientes, especialidades):
    from asignar_turno import mostrar_especialidades, obtener_especialidad
    while True:
        print("\n--- Atender siguiente turno ---")
        mostrar_especialidades()
        opcion = input("Seleccione especialidad: ")
        especialidad = obtener_especialidad(opcion)
        if especialidad is None:
            print("Opción inválida. Intente de nuevo.")
            continue
        break

    turno = obtener_siguiente_turno(especialidad, turnos)

    if turno is None:
        print(f"No hay turnos pendientes en {especialidad}.")
        return

    mostrar_siguiente_turno(turno, pacientes)
    nuevo_estado = seleccionar_nuevo_estado()
    turno["estado"] = nuevo_estado
    especialidades[especialidad]["turnos_asignados"] -= 1
    print(f"Turno #{turno['id_turno']} marcado como {nuevo_estado}.")

#------------------------------------------------------------------------------------

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