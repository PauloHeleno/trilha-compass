"""Escreva um código Python para imprimir todos os números primos entre 1 até 100.
 Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não."""

numero_divisao = 0

for numero in range(1, 101):
    for divisor in range(1, (numero + 1)):
        if numero % divisor == 0:
            numero_divisao += 1
    if numero_divisao == 2:
        print(numero)
        numero_divisao = 0
    else:
        numero_divisao = 0