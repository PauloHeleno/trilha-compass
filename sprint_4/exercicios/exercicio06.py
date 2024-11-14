def maiores_que_media(conteudo:dict)->list:

    media = sum(conteudo.values()) / len(conteudo)
    
    valores = list(filter(lambda item: item[1] > media, conteudo.items()))
    
    valores.sort(key=lambda x: x[1])

    return valores


dicionario = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

print(maiores_que_media(dicionario))
