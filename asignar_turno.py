def mostrar_especialidades():
    print("1. Clínica médica")
    print("2. Pediatría")
    print("3. Traumatología")
    print("4. Cardiología")
    print("5. Guardia")


def obtener_especialidad(opcion):
    match opcion:
        case "1":
            return "Clinica medica"
        case "2":
            return "Pediatria"
        case "3":
            return "Traumatologia"
        case "4":
            return "Cardiologia"
        case "5":
            return "Guardia"
        case _:
            return None


def hay_disponibilidad(especialidad, especialidades):
    return especialidades[especialidad]["turnos_asignados"] < especialidades[especialidad]["cupo_maximo"]


def mostrar_prioridades():
    print("1. Alta")
    print("2. Media")
    print("3. Baja")


def asignar_prioridad(opcion):
    match opcion:
        case "1":
            return "Alta"
        case "2":
            return "Media"
        case "3":
            return "Baja"
        case _:
            return None


def ocupar_turno(especialidad, dni, prioridad, especialidades, turnos):
    especialidades[especialidad]["turnos_asignados"] += 1
    turno = {
        "id_turno":     len(turnos) + 1,
        "dni":          dni,
        "especialidad": especialidad,
        "prioridad":    prioridad,
        "estado":       "pendiente"
    }
    turnos.append(turno)
