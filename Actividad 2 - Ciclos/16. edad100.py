suma_edades = 0
cantidad = 0

print("Ingrese edades. El programa terminará cuando se ingrese una edad mayor a 100.\n")

while True:
    entrada = input("Ingrese una edad: ")

    try:
        edad = int(entrada)

        if edad > 100:
            break

        if edad < 0:
            print("La edad no puede ser negativa. Intente de nuevo.")
            continue

        suma_edades += edad
        cantidad += 1

    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if cantidad > 0:
    promedio = suma_edades / cantidad
    print(f"\nSe ingresaron {cantidad} edades válidas.")
    print(f"El promedio de las edades es: {promedio:.2f}")
else:
    print("\nNo se ingresaron edades válidas.")
