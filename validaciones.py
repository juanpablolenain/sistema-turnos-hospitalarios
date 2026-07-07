# Funciones para validar los datos ingresados por el usuario antes de registrarlos.
# Cada función recibe un string y devuelve True si es válido, False si no lo es.
# En caso de error, imprime un mensaje descriptivo para que el usuario sepa qué corregir.

def validar_dni(dni):
    # El DNI no puede estar vacío, debe contener solo números y tener 7 u 8 dígitos
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
    # El nombre no puede estar vacío, debe tener al menos 2 caracteres y solo letras y espacios
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
    # La edad debe ser un número entero entre 0 y 120
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
    # Solo se aceptan las obras sociales con las que trabaja el centro
    obras_social_aceptadas = ["OSDE", "ISSUNNE", "INSSEP", "PARTICULAR"]
    obra_social = obra_social.upper()
    if obra_social in obras_social_aceptadas:
        return True
    else:
        print("Error: El estudio no trabaja con la obra social: ", obra_social)
        print("Opciones válidas: ", obras_social_aceptadas)
        return False

