def imprime_parametros(*args, **kwargs):
    
    for parametro in args:
        print(parametro)
    
    for nome, valor in kwargs.items():
        print(f"{valor}")


imprime_parametros(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
