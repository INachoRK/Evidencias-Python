clave_correcta = "secreta123"

intento = ""

while intento != clave_correcta:
    intento = input("Ingrese la contraseña: ")

    if intento != clave_correcta:
        print("Contraseña incorrecta. Intente de nuevo.\n")

print("¡Acceso concedido! 🎉")
