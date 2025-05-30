suma = 0

for i in range(5):
    while True:
        entrada = input(f"Ingrese el número {i + 1}: ")
        try:
            numero = float(entrada)
            suma += numero
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

promedio = suma / 5

print("El promedio de los 5 números es:", promedio)
