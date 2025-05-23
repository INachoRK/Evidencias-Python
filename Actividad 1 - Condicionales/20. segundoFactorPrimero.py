def esFactor(dividendo, divisor):
    if divisor == 0:
        return False
    return dividendo % divisor == 0

def main():
    try:
        num1 = int(input("Ingrese el primer número (dividendo): "))
        num2 = int(input("Ingrese el segundo número (posible factor): "))

        if esFactor(num1, num2):
            print(f"El número {num2} es un factor de {num1}.")
        else:
            print(f"El número {num2} NO es un factor de {num1}.")
    except ValueError:
        print("Debe ingresar números enteros válidos.")

if __name__ == "__main__":
    main()
