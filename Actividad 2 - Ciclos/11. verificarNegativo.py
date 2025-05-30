suma_total = 0

print("Ingrese números uno por uno. El programa terminará si escribe un número negativo.\n")

while True:
    entrada = input("Ingrese un número: ")

    try:
        numero = float(entrada)

        if numero < 0:
            break

        suma_total += numero

    except ValueError:
        print("Por favor, ingrese un número válido.")

print("La suma total de los números ingresados es:", suma_total)
