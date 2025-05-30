a = 0
b = 1

print("Serie de Fibonacci hasta que el valor supere los 1000:")

while a <= 1000:
    print(a)
    siguiente = a + b
    a = b
    b = siguiente
