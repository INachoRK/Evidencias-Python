def esPar(numero):
    return numero % 2 == 0

def sumaEsPar(a, b, c):
    suma = a + b + c
    return esPar(suma)

def main():
    try:
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        c = int(input("Ingrese el tercer número: "))
        resultado = a + b + c

        if sumaEsPar(a, b, c):
            print(f"La suma de {a}, {b}, {c} es par y su resultado es: {resultado}")
        else:
            print(f"La suma de {a}, {b}, {c} es impar y su resultado es: {resultado}")
    except ValueError:
        print("Debe ingresar solo valores numéricos")

if __name__ == "__main__":
    main()