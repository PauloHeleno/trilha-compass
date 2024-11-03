
numeros = []

for numero in range(1, 4):
    numeros.append(numero)

# Verifica cada número se é par ou ímpar
for numero in numeros:
    if numero % 2 == 0:
        print("Par:", numero)
    else:
        print("Ímpar:", numero)
