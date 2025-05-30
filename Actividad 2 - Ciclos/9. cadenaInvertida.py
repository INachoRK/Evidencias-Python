cadena = input("Ingrese una cadena: ")

invertida = ""

longitud = len(cadena)
for i in range(longitud - 1, -1, -1):
    invertida += cadena[i]

print("Cadena invertida:", invertida)
