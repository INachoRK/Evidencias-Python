from datetime import date

def esMayor(edad):
    return edad >= 18

def main():
    try:
        anioNacimiento = int(input("Ingrese su año de nacimiento: "))
        anioActual = date.today().year
        edad = anioActual - anioNacimiento

        if esMayor(edad):
            print(f"Su año de nacimiento es {anioNacimiento}, su edad aproximada es {edad}. Usted puede votar.")
        else:
            print(f"Su año de nacimiento es {anioNacimiento}, su edad aproximada es {edad}. Usted no puede votar.")
    except ValueError:
        print("Debe ingresar un año de nacimiento válido")

if __name__ == "__main__":
    main()
