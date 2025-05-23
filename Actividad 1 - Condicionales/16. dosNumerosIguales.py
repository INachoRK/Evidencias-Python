def dosNumerosIguales(numero):
    numeroStr = str(abs(numero))
    conteo = {}

    for digito in numeroStr:
        conteo[digito] = conteo.get(digito, 0) + 1

    repeticionesDosVeces = sum(1 for cantidad in conteo.values() if cantidad == 2)

    return repeticionesDosVeces == 1

def main():
    try:
        numero = int(input("Ingrese un número: "))

        if dosNumerosIguales(numero):
            print(f"El número {numero} tiene exactamente dos dígitos iguales.")
        else:
            print(f"El número {numero} NO tiene exactamente dos dígitos iguales.")
    except ValueError:
        print("Debe ingresar un número entero válido.")

if __name__ == "__main__":
    main()
