cantidad = 10

a = 0
b = 1

print("Los primeros 10 números de la serie de Fibonacci son:")

for i in range(cantidad):
    print(a)
    siguiente = a + b
    a = b
    b = siguiente
