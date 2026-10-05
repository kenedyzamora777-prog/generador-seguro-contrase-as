import secrets
import string


def mostrar_menu():
    """Muestra el menú principal del programa."""
    print("\n===== GENERADOR SEGURO DE CONTRASEÑAS =====")
    print("1. Generar contraseña")
    print("2. Salir")


def solicitar_longitud():
    """Solicita y valida la longitud de la contraseña."""
    while True:
        try:
            longitud = int(input("Ingrese la longitud de la contraseña (8-50): "))

            if 8 <= longitud <= 50:
                return longitud

            print("Error: la longitud debe estar entre 8 y 50 caracteres.")
        except ValueError:
            print("Error: debe ingresar un número entero.")


def generar_contrasena(longitud):
    """Genera una contraseña usando letras, números y símbolos."""
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation

    # Se garantiza al menos un carácter de cada tipo.
    caracteres_obligatorios = [
        secrets.choice(letras),
        secrets.choice(numeros),
        secrets.choice(simbolos)
    ]

    todos = letras + numeros + simbolos

    restantes = [
        secrets.choice(todos)
        for _ in range(longitud - len(caracteres_obligatorios))
    ]

    caracteres = caracteres_obligatorios + restantes

    # secrets.SystemRandom permite mezclar los caracteres de forma segura.
    secrets.SystemRandom().shuffle(caracteres)

    return "".join(caracteres)


def ejecutar_programa():
    """Controla el funcionamiento principal del programa."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            longitud = solicitar_longitud()
            contrasena = generar_contrasena(longitud)

            print("\nContraseña generada:")
            print(contrasena)

        elif opcion == "2":
            print("Programa finalizado. Gracias por utilizarlo.")
            break

        else:
            print("Opción no válida. Seleccione 1 o 2.")


if __name__ == "__main__":
    ejecutar_programa()
