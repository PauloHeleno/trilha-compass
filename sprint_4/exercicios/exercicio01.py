with open('number.txt', 'r') as arquivo:
    
    linhas = arquivo.readlines()

    pares = list(filter(lambda x: x % 2 == 0, map(lambda x: int(x.strip()), linhas)))

    top_5 = sorted(pares, reverse=True)[:5]

    soma = sum(top_5)

    print(top_5)

    print(soma)