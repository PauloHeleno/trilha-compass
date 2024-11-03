def funcao(string):
    lista = string.split(',')
    soma = 0
    for numero in lista:
        soma += int(numero)
    return soma



print(funcao("1,3,4,6,10,76"))



