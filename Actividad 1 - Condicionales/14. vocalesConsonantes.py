def vocalesConsonantes(palabra):
    vocales = 'aeiou'
    palabra = palabra.lower()

    cant_vocales = 0
    cant_consonantes = 0

    for letra in palabra:
        if letra.isalpha():
            if letra in vocales:
                cant_vocales += 1
            else:
                cant_consonantes += 1

    return cant_vocales == cant_consonantes

def main():
    palabra = input("Ingrese una palabra o frase: ")

    if vocalesConsonantes(palabra):
        print(f"La palabra/frase '{palabra}' tiene la misma cantidad de vocales y consonantes.")
    else:
        print(f"La palabra/frase '{palabra}' NO tiene la misma cantidad de vocales y consonantes.")

if __name__ == "__main__":
    main()
