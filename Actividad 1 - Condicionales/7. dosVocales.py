def vocalesDistintas(palabra):
    vocales = set()
    for letra in palabra.lower():
        if letra in 'aeiou':
            vocales.add(letra)
    return len(vocales) >= 2

def main():
    palabra = input("Ingrese una palabra: ")

    if vocalesDistintas(palabra):
        print(f"La palabra '{palabra}' tiene al menos dos vocales distintas.")
    else:
        print(f"La palabra '{palabra}' NO tiene al menos dos vocales distintas.")

if __name__ == "__main__":
    main()
