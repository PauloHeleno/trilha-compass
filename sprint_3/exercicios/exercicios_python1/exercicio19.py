import random

random_list = random.sample(range(500), 50)

random_list = sorted(random_list)

mediana = (random_list[50//2 - 1] + random_list[50//2]) / 2
media = sum(random_list) / 50
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}' )

