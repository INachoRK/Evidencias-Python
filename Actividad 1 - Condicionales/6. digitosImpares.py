def esCantidadImparDeDigitos(numero):
    cantidad = len(str(abs(numero)))
    return cantidad % 2 != 0

def main():
    try:
        numero = int(input("Ingrese un número: "))
        if esCantidadImparDeDigitos(numero):
            print(f"El número {numero} tiene una cantidad impar de dígitos.")
        else:
            print(f"El número {numero} tiene una cantidad par de dígitos.")
    except ValueError:
        print("Debe ingresar un número válido.")

if __name__ == "__main__":
    main()
