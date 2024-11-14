with open('estudantes.csv', 'r') as arquivo:
    linhas = arquivo.readlines()

    resultados = list(map(lambda linha: (
        linha.strip().split(',')[0],
        sorted(map(int, linha.strip().split(',')[1:6]), reverse=True)[:3]
    ), linhas))

    resultados = [(nome, notas, round(sum(notas) / 3, 2)) for nome, notas in resultados]

    resultados.sort(key=lambda x: x[0])

    saidas = [f"Nome: {nome} Notas: {notas}\nMédia: {media}" for nome, notas, media in resultados]

    print("\n".join(saidas))
