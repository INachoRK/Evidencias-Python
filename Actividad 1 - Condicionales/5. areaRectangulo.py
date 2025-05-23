def areaMayor(area):
    return area > 100

def main():
    try:
        a = float(input("Ingrese el ancho del rectángulo: "))
        b = float(input("Ingrese el largo del rectángulo: "))
        area = a * b

        if  areaMayor(area):
            print(f"El área tiene un valor de {area} y es mayor a 100")
        else:
            print(f"El área tiene un valor de {area} y es menor o igual a 100")
    except ValueError:
        print("Debe ingresar valores numéricos para calcular el área de un rectángulo")

if __name__ == "__main__":
    main()