
def remove_duplicados(lista):
    nova_lista = set(lista)
    nova_lista = list(nova_lista)
    return nova_lista


print(remove_duplicados(['abc', 'abc', 'abc', '123', 'abc', '123', '123']))
