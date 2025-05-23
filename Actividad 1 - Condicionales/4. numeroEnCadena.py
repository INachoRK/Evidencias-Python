def contieneNumero(texto):
    for i in texto:
        if i.isdigit():
            return True
    return False

def main():
    texto = "Ingrese el texto que desea analizar: "

    if contieneNumero(texto):
        print("El texto contiene al menos un número")
    else:
        print("El texto no contiene ningún número")

if __name__ == "__main__":
    main()
