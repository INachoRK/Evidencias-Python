def vocalesRequeridas(cadena):
    vocales = set('aeiou')
    vocalesEncontradas = set(c for c in cadena.lower() if c in vocales)
    return vocalesEncontradas == vocales

def main():
    texto = input("Ingrese una frase o palabra: ")

    if vocalesRequeridas(texto):
        print("La cadena contiene todas las vocales (a, e, i, o, u).")
    else:
        print("La cadena NO contiene todas las vocales.")

if __name__ == "__main__":
    main()
