def MultiploO9(numero):
    return numero % 9 == 0 or '9' in str(abs(numero))

def main():
    try:
        numero = int(input("Ingrese un número entero: "))

        if MultiploO9(numero):
            print(f"El número {numero} es múltiplo de 9 o contiene el dígito 9.")
        else:
            print(f"El número {numero} NO es múltiplo de 9 ni contiene el dígito 9.")
    except ValueError:
        print("Debe ingresar un número entero válido.")

if __name__ == "__main__":
    main()
