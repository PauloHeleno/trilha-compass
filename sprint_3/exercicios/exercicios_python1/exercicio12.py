def potencia(lista):
    
    nova_lista = []

    for numero in lista:
        nova_lista.append(numero**2)

    return nova_lista


def my_map(list, f):
    
    return f(list)


print(my_map([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],potencia ))