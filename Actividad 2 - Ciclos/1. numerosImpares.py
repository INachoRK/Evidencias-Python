suma_impares = 0

for numero in range(1, 101):
    if numero % 2 != 0:
        suma_impares += numero

print("La suma de los números impares del 1 al 100 es:", suma_impares)
