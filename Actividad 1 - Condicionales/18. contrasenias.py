def es_contrasena_fuerte(contrasena):
    tieneMayuscula = any(c.isupper() for c in contrasena)
    tieneMinuscula = any(c.islower() for c in contrasena)
    tieneNumero = any(c.isdigit() for c in contrasena)
    longitudValida = len(contrasena) >= 8

    return tieneMayuscula and tieneMinuscula and tieneNumero and longitudValida

def main():
    contrasena = input("Ingrese una contraseña: ")

    if es_contrasena_fuerte(contrasena):
        print("La contraseña es fuerte.")
    else:
        print("La contraseña NO es fuerte. Debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número.")

if __name__ == "__main__":
    main()
