def esInicial(letra, palabra):
    return palabra.lower().startswith(letra.lower())

def main():
    letra = input("Ingrese una letra: ")
    palabra = input("Ingrese una palabra: ")

    if len(letra) != 1 or not letra.isalpha():
        print("Debe ingresar solo una letra válida.")
        return

    if esInicial(letra, palabra):
        print(f"La letra '{letra}' es la inicial de la palabra '{palabra}'.")
    else:
        print(f"La letra '{letra}' NO es la inicial de la palabra '{palabra}'.")

if __name__ == "__main__":
    main()
