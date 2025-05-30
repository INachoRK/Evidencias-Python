entrada = input("Ingrese un número entero mayor que 1: ")

if entrada.isdigit():
    numero = int(entrada)

    if numero <= 1:
        print("El número debe ser mayor que 1.")
    else:
        es_primo = True
        divisor = 2

        while divisor * divisor <= numero:
            if numero % divisor == 0:
                es_primo = False
                break
            divisor += 1

        if es_primo:
            print(f"{numero} es un número primo.")
        else:
            print(f"{numero} no es un número primo.")
else:
    print("Por favor, ingrese un número entero válido.")
