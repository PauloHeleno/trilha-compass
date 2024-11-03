def divide_lista(lista):
    tamanho = len(lista) // 3
    

    lista1 = lista[0:tamanho]
    lista2 = lista[tamanho:2 * tamanho]
    lista3 = lista[2 * tamanho:]
    
    return lista1, lista2, lista3


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
resultado = divide_lista(lista)
print(*resultado)
