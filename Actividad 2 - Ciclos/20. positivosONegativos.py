positivos = 0
negativos = 0
ceros = 0

print("Ingrese 10 números (positivos, negativos o ceros):\n")

for i in range(1, 11):
    while True:
        entrada = input(f"Número {i}: ")

        try:
            numero = float(entrada)

            if numero > 0:
                positivos += 1
            elif numero < 0:
                negativos += 1
            else:
                ceros += 1

            break

        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

print("\nResultados:")
print("Positivos:", positivos)
print("Negativos:", negativos)
print("Ceros:", ceros)
