# Desafio Sprint 5


## 📋 **Descrição do desafio e o meu passo a passo**  
Objetivo: praticar os conhecimentos de AWS aprendidos na sprint.

## Inicialmente escolhi um arquivo.csv chamado "producao-mar-2024.csv" no portal de dados publicos do Governo brasileiro

![producao-mar-2024](../evidencias/print_desafio/producao-mar-2024.png)

## Depois disso, criei um bucket no s3 chamado "bucket-desafio.com"

![bucket_inicial](../evidencias/print_desafio/bucket_inicio.png)

## Em seguida, baixei o aws cli e o boto3

![cli_boto3](../evidencias/print_desafio/cli_boto3.png)

## Após isso, criei um profile chamado "Paulo Heleno" com aws consigure sso e loguei na minha conta aws console através dele

![sso](../evidencias/print_desafio/sso_login.png)

## Requisição foi aceita

![requisição](../evidencias/print_desafio/imagem_requisi.png)

## Para confirar se tudo estava certo, utilizei o seguinte comando abaixo. O comando serve para listar os buckets que estão no meu s3

![ls_s3](../evidencias/print_desafio/ls_bucket.png)

## Por conseguinte, criei um script chamado "upload_arquivo.py", a função desse script é subir o "producao-mar-2024.csv" pro nosso bucket. Após a criação ele foi executado, coloquei alguns prints para facilitar a visualização

![upload](../evidencias/print_desafio/upload_arquivo_rodando.png)

## Logo em seguida, criei um outro script chamado "script_dataframe.py" que tem como objetivo baixar o arquivo csv do bucket, gerar um dataframe e um arquivo.csv chamado "dados_processados" a partir do dataframe. O dataframe tem os seguintes requisitos:
## OBS: todas as funções abaixo retornam somente uma resposta

    - uma clausula que filtra dados usando ao menos dois operadores lógicos
    - duas funções de agregação
    - uma função condicional
    - uma função de conversão
    - uma função de data
    - uma função de string

![dataframe](../evidencias/print_desafio/script_dataframe.png)

## Execução do script e o arquivo "dados_processados" que foi gerado a partir dele, coloquei prints para facilitar a visualização

![rodandoDataFrame](../evidencias/print_desafio/rodando_dataframe_dados_processados.png)

## Arquivos no bucket ao final do desafio

![bucket_finalizado](../evidencias/print_desafio/bucket_final.png)


