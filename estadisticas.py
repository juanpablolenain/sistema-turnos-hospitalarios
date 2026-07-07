from atender_turno import ORDEN_PRIORIDAD


def ver_estadisticas(turnos, especialidades, pacientes):
    if not turnos:
        print("\nNo hay turnos registrados en el día.")
        return

    total      = len(turnos)
    atendidos  = len([t for t in turnos if t["estado"] == "atendido"])
    pendientes = len([t for t in turnos if t["estado"] == "pendiente"])
    ausentes   = len([t for t in turnos if t["estado"] == "ausente"])
    cancelados = len([t for t in turnos if t["estado"] == "cancelado"])

    print("\n========== Estadísticas del día ==========")
    print(f"\nTotal de turnos asignados: {total}")
    print(f"  Atendidos:  {atendidos}")
    print(f"  Pendientes: {pendientes}")
    print(f"  Ausentes:   {ausentes}")
    print(f"  Cancelados: {cancelados}")
    print("\n==========================================")
