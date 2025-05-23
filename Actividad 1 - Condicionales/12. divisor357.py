def divisible357(numero):
    return numero % 3 == 0 and numero % 5 == 0 and numero % 7 == 0

def main():
    try:
        numero = int(input("Ingrese un número entero: "))

        if divisible357(numero):
            print(f"El número {numero} es divisible entre 3, 5 y 7.")
        else:
            print(f"El número {numero} NO es divisible entre 3, 5 y 7.")
    except ValueError:
        print("Debe ingresar un número entero válido.")

if __name__ == "__main__":
    main()
