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

    print("\n--- Por especialidad ---")
    for especialidad in especialidades:
        turnos_esp = [t for t in turnos if t["especialidad"] == especialidad]
        if not turnos_esp:
            continue
        atendidos_esp  = len([t for t in turnos_esp if t["estado"] == "atendido"])
        pendientes_esp = len([t for t in turnos_esp if t["estado"] == "pendiente"])
        ausentes_esp   = len([t for t in turnos_esp if t["estado"] == "ausente"])
        cancelados_esp = len([t for t in turnos_esp if t["estado"] == "cancelado"])
        print(f"\n  {especialidad}:")
        print(f"    Atendidos:  {atendidos_esp}")
        print(f"    Pendientes: {pendientes_esp}")
        print(f"    Ausentes:   {ausentes_esp}")
        print(f"    Cancelados: {cancelados_esp}")

    print("\n--- Por prioridad ---")
    for prioridad in sorted(ORDEN_PRIORIDAD, key=lambda p: ORDEN_PRIORIDAD[p]):
        turnos_prio    = [t for t in turnos if t["prioridad"] == prioridad]
        atendidos_prio = len([t for t in turnos_prio if t["estado"] == "atendido"])
        total_prio     = len(turnos_prio)
        print(f"  {prioridad}: {total_prio} asignados, {atendidos_prio} atendidos")

    print("\n--- Pacientes registrados ---")
    print(f"  Total: {len(pacientes)}")

    print("\n==========================================")
