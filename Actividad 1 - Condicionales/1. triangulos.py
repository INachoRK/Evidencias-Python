def esTriangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a

def clasificarTriangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isóceles"
    else:
        return "Escaleno"

def main():
    try:
        a = float(input("Ingrese el lado a: "))
        b = float(input("Ingrese el lado b: "))
        c = float(input("Ingrese el lado c: "))

        if esTriangulo(a, b, c):
            tipo = clasificarTriangulo(a, b, c)
            print(f"Es un triángulo {tipo}")
        else:
            print("No se puede formar un triángulo")
    except ValueError:
        print("No se pueden ingresar datos diferentes a números")

if __name__ == "__main__":
    main()
