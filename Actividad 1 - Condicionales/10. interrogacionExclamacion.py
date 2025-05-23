def terminaConSigno(frase):
    return frase.endswith("!") or frase.endswith("?")

def main():
    frase = input("Ingrese una frase: ")

    if terminaConSigno(frase):
        print("La frase termina en un signo de exclamación o interrogación.")
    else:
        print("La frase NO termina en un signo de exclamación ni interrogación.")

if __name__ == "__main__":
    main()
