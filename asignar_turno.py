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


def hay_disponibilidad(especialidad):
    return especialidades[especialidad]["turnos_asignados"] < especialidades[especialidad]["cupo_maximo"]


def ocupar_turno(especialidad):
    especialidades[especialidad]["turnos_asignados"] += 1