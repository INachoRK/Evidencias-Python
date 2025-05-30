contador = 0

print("Ingrese números uno por uno. El programa se detiene cuando escriba 0.\n")

while True:
    entrada = input("Ingrese un número: ")

    try:
        numero = float(entrada)

        if numero == 0:
            break

        contador += 1

    except ValueError:
        print("Por favor, ingrese un número válido.")

print("Se ingresaron", contador, "números antes de escribir 0.")
