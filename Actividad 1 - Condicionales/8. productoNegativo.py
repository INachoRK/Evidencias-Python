def productoNegativo(a, b):
    return a * b < 0

def main():
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))

        if productoNegativo(a, b):
            print(f"El producto de {a} y {b} es negativo.")
        else:
            print(f"El producto de {a} y {b} NO es negativo.")
    except ValueError:
        print("Debe ingresar valores numéricos.")

if __name__ == "__main__":
    main()
