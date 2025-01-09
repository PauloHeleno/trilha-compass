import random
import names
import time
import os

# etapa 1

lista = [random.randint(1, 1000) for _ in range(250)]

lista.reverse()

print(lista)


# etapa 2

animais = [
    "Elefante", "Cachorro", "Gato", "Leao", "Tigre", 
    "Macaco", "Cobra", "Jacare", "Zebra", "Cavalo",
    "Pato", "Peixe", "Urso", "Coelho", "Girafa", 
    "Porco", "Camelo", "Arraia", "Lobo", "Raposa"
]

animais.sort()

[print(animal) for animal in animais]

with open("animais.csv", "w", encoding="utf-8") as arquivo:
    arquivo.write("\n".join(animais))


# etapa 3

random.seed(40)

qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10_000_000

aux = []

for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())
    
print("Gerando {} nomes aleatorios".format(qtd_nomes_aleatorios))

dados = []

for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

with open("nomes_aleatorios.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("\n".join(dados))
