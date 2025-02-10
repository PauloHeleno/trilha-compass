# Desafio Sprint 10


## 📋 **Descrição do desafio e o meu passo a passo**  
Objetivo: O objetivo é criar um dashboard no AWS QuickSight para visualizar insights dos dados armazenados na camada Refined do data lake, usando o Athena como fonte de dados.

### Inicialmente, comecei criando um DataSet no AWS QuickSight a partir das tabelas que criei no AWS Athena durante a Sprint 9. Meu DataSet ficou composto por duas tabelas: uma tabela fato e uma tabela de dimensão para os filmes.

### Após isso, apliquei um join entre as duas tabelas para unificá-las e permitir o acesso às colunas de ambas.

![Join](../evidencias/print_desafio/Join.png)

### Depois disso, criei um filtro para poder pegar apenas filmes com o "Ano de lançamento" acima de 2000.

![Filtro](../evidencias/print_desafio/Filtro.png)

### Abaixo, segue a imagem do DataSet criado no QuickSight:

![Meu Data Set](../evidencias/print_desafio/DataSet_criado.png)

### Em seguida, iniciei uma análise no QuickSight através do meu DataSet para criar meu DashBoard.

### Primeiramente escolhi o título do meu dashboard.

![Titulo](../evidencias/print_desafio/Titulo.png)

### Logo após, criei 6 KPI (Key Performance Indicator).

### Agora um pouco sobre cada uma:

1. **🎞️ Quantidade de filmes analisados**  
   - Exibe o total de filmes incluídos na análise.

2. **💰 Filme com a maior receita**  
   - Mostra o filme que gerou a maior receita total.

3. **⭐ Filme com a maior nota média**  
   - Exibe o filme com a melhor avaliação média do público.

4. **🗳️ Filme com o maior número de votos**  
   - Destaca o filme com a maior quantidade de avaliações registradas.

5. **⏳ Filme com a maior duração (minutos)**  
   - Indica o filme mais longo da análise.

6. **🌍 País de produção com maior lucro médio**  
   - Revela o país cujos filmes tiveram, em média, o maior lucro.

### Essas são as KPIs:

![KPIs](../evidencias/print_desafio/KPS.png)

### Por conseguinte, criei 4 gráficos para minha análise.

### O primeiro tem o intuito de comparar orçamento e duração dos filmes para dentificar se filmes com maior orçamento tendem a ser mais longos ou curtos.

### Para ajudar na vizualização desse gráfico, criei uma coluna para classificar os filmes como curto, médio ou longo de acordo com o tempo de cada filme. Logo abaixo, o pequeno trecho de código que foi usado.

![Classificação](../evidencias/print_desafio/classificacao.png)

### O gráfico:

![Orçamento e tempo](../evidencias/print_desafio/Grafico_investimento_tempo.png)

### O segundo tem o intuito de avaliar se filmes com as maiores receitas também são os mais populares.

![Popularidade e receita](../evidencias/print_desafio/Filmes_mais_lucrativos.png)

### O terceiro tem o intuito de descobrir se filmes com mais votos são os que têm as melhores notas. Isso pode indicar se um filme amplamente avaliado é geralmente bem recebido pelo público.

![Votos](../evidencias/print_desafio/numero_de_votos.png)

### O quarto tem o intuito de ver quais países produzem os filmes mais lucrativos e se há um padrão geográfico de sucesso. 

![Países e lucro](../evidencias/print_desafio/Países_lucrativos.png)

### Por fim, feito tudo isso, esse foi o resultado final do meu DashBoard: 

![DashBoard](../evidencias/print_desafio/dash_completo.png)

### Ele salvo no QuickSight:

![Dash QuickSight](../evidencias/print_desafio/Dash_No_quick.png)
