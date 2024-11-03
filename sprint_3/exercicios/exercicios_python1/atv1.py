from datetime import datetime

nome = "Alice"
idade = 25

# Pegando o ano atual
ano_atual = datetime.now().year

# calxulo do ano
ano_completa_100 = ano_atual + (100 - idade)

print(ano_completa_100)

