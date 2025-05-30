entrada = input("Ingresa un número entero positivo: ")

if entrada.isdigit():
    numero = int(entrada)

    print(f"Los divisores de {numero} son:")

    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)
else:
    print("Por favor, ingresa un número entero positivo válido.")
