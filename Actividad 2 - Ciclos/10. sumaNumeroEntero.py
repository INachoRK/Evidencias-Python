entrada = input("Ingrese un número entero positivo: ")

if entrada.isdigit():
    suma = 0

    for caracter in entrada:
        suma += int(caracter)

    print("La suma de los dígitos es:", suma)
else:
    print("Entrada inválida. Por favor, ingrese solo números enteros positivos.")
