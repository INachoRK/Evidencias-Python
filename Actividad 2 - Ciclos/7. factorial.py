entrada = input("Ingrese un número entero no negativo: ")

if entrada.isdigit():
    numero = int(entrada)
    factorial = 1

    for i in range(1, numero + 1):
        factorial *= i

    print(f"El factorial de {numero} es: {factorial}")
else:
    print("Por favor, ingrese un número entero no negativo válido.")
