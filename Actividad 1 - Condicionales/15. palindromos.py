def esPalindromo(cadena):
    cadena = ''.join(c for c in cadena.lower() if c.isalnum())
    return cadena == cadena[::-1]

def main():
    texto = input("Ingrese una palabra o frase: ")

    if esPalindromo(texto):
        print(f"La cadena '{texto}' es un palíndromo.")
    else:
        print(f"La cadena '{texto}' NO es un palíndromo.")

if __name__ == "__main__":
    main()
