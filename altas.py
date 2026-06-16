from validaciones import validar_dni, validar_nombre, validar_edad, validar_obra_social

def registrar_paciente(pacientes):
    print("\n--- Registro de paciente ---")
    while True:
        dni = input("Ingrese DNI: ").strip()
        if validar_dni(dni):
            break
    if dni in pacientes:
        print("Error: ya existe un paciente registrado con ese DNI.")
        return
    while True:
        nombre = input("Ingrese nombre y apellido: ").strip()
        if validar_nombre(nombre):
            break
    while True:
        edad = input("Ingrese edad: ").strip()
        if validar_edad(edad):
            break
    while True:
        obra_social = input("Ingrese obra social o escriba Particular: ").strip().upper()
        if validar_obra_social(obra_social):
            break
    pacientes[dni] = {
        "nombre": nombre,
        "edad": int(edad),
        "obra_social": obra_social
    }
    print("Paciente registrado correctamente.")
