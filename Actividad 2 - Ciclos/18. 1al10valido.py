while True:
    entrada = input("Ingrese un número entre 1 y 10: ")

    if entrada.isdigit():
        numero = int(entrada)

        if 1 <= numero <= 10:
            print(f"¡Perfecto! Ingresaste el número {numero}.")
            break
        else:
            print("El número está fuera del rango. Intenta de nuevo.\n")
    else:
        print("Entrada inválida. Por favor, ingrese un número entero.\n")
