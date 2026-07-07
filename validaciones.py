#CONSTANTE GLOBALES
OBRAS_SOCIALES_ACEPTADAS = ["OSDE", "ISSUNNE", "INSSEP", "PARTICULAR"]

def mostrar_obras_sociales():
    print("Obras sociales aceptadas:")

    for obra_social in OBRAS_SOCIALES_ACEPTADAS:
        print("-", obra_social)

def validar_dni(dni):
    if dni == "":
        print("Error: el DNI no puede estar vacío.")
        return False
    if not dni.isdigit():
        print("Error: el DNI debe contener solo números.")
        return False
    if len(dni) < 7 or len(dni) > 8:
        print("Error: el DNI debe tener 7 u 8 dígitos.")
        return False
    return True

def validar_nombre(nombre):
    if nombre == "":
        print("Error: el nombre no puede estar vacío.")
        return False
    if len(nombre) < 2:
        print("Error: el nombre es demasiado corto.")
        return False
    for caracter in nombre:
        if not (caracter.isalpha() or caracter == " "):
            print("Error: el nombre solo puede contener letras y espacios.")
            return False
    return True

def validar_edad(edad):
    if edad == "":
        print("Error: la edad no puede estar vacía.")
        return False

    if not edad.isdigit():
        print("Error: la edad debe ser un número.")
        return False

    edad = int(edad)

    if edad < 0 or edad > 120:
        print("Error: la edad debe estar entre 0 y 120 años.")
        return False

    return True

def validar_obra_social(obra_social):
    obra_social = obra_social.upper()
    if obra_social in OBRAS_SOCIALES_ACEPTADAS:
        return True
    else:
        print("Error: El estudio no trabaja con la obra social: ", obra_social)
        return False