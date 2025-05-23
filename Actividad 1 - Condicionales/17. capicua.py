def esCapicua(numero):
    numeroStr = str(abs(numero))
    return numeroStr == numeroStr[::-1]

def main():
    try:
        numero = int(input("Ingrese un número entero: "))

        if esCapicua(numero):
            print(f"El número {numero} es capicúa.")
        else:
            print(f"El número {numero} NO es capicúa.")
    except ValueError:
        print("Debe ingresar un número entero válido.")

if __name__ == "__main__":
    main()
