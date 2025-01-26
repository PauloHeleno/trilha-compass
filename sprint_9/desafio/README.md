# Desafio Sprint 9


## 📋 **Descrição do desafio e o meu passo a passo**  
Objetivo: Estruturar dados na camada Refined Zone seguindo princípios de modelagem multidimensional, utilizando o AWS Glue Data Catalog para criar tabelas 


## Inicialmente eu comecei criando um job chamado "unir_parquets", que utiliza Apache Spark para processar e transformar dados de duas fontes no formato Parquet, localizadas na camada Trusted do Data Lake, e salvá-los na camada Refined em formato Parquet.

## Resumo do processo:

### Lê dois arquivos de dados Parquet: um local (caminho_local) e outro do TMDb (caminho_tmdb).

![script começo](../evidencias/print_desafio/script_comeco.png)

### Realiza um join entre os datasets com base em id_no_imdb e id_local, filtrando apenas registros com orçamento e receita não nulos.

### Calcula o lucro como Receita - Orçamento.

### Cria duas tabelas, uma "Fato" e a "dim_filme"

### Fato: Contém métricas como lucro, receita, orçamento e popularidade.

### Dim_filme: Contém informações sobre os filmes, como título, duração e país de produção.

### Remove duplicados e divide em arquivos otimizados usando coalesce(1).

![script meio](../evidencias/print_desafio/script_meio.png)

### Salva as tabelas Fato e Dim_Filme no Data Lake na camada Refined no formato parquet, os arquivos particionados por ano, mês e dia.

![script fim](../evidencias/print_desafio/script_fim.png)

## Agora, o meu diagrama dimensional para facilitar a visualização de como ficou a estrutura das tabelas.

![diagrama dimensional](../evidencias/print_desafio/diagrama_dimensional.png)

## Execução do meu job, repare nas configurações do mesmo de acordo com a documentação do desafio.

![executando job](../evidencias/print_desafio/execucao_job.png)

## Arquivo parquet que representa a tabela fato gerado no bucket

![tabela fato bucket](../evidencias/print_desafio/caminho_fato.png)

## Arquivo parquet que representa a tabela dim_filme gerado no bucket

![tabela dim_filme bucket](../evidencias/print_desafio/caminho_dim_filme.png)

## Depois de executar o job, criei e executei um crawler para a criação das tabelas no aws glue catalog.

![crawler](../evidencias/print_desafio/crawler.png)

## Resultado com as tabelas criadas a partir do crawler

![tabelas](../evidencias/print_desafio/tabelas_criadas.png)

## Depois conferi o conteúdo das tabelas clicando em table data

## Conteúdo da tabela fato:

![select fato](../evidencias/print_desafio/select_fato.png)

![resultado fato](../evidencias/print_desafio/resultado_fato.png)

## Conteúdo da tabela Dim_filme:

![select dim_filme](../evidencias/print_desafio/select_dim_filmes.png)

![resultado dim_filme](../evidencias/print_desafio/resultado_dim_filmes.png)
