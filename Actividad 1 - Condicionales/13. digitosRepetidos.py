def digitosRepetidos(numero):
    numeroStr = str(abs(numero))
    return len(set(numeroStr)) < len(numeroStr)

def main():
    try:
        numero = int(input("Ingrese un número entero: "))

        if digitosRepetidos(numero):
            print(f"El número {numero} tiene dígitos repetidos.")
        else:
            print(f"El número {numero} NO tiene dígitos repetidos.")
    except ValueError:
        print("Debe ingresar un número entero válido.")

if __name__ == "__main__":
    main()
