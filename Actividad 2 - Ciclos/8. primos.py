print("Números primos entre 1 y 50:")

for num in range(2, 51):
    es_primo = True

    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            es_primo = False
            break

    if es_primo:
        print(num)
