# Desafio Sprint 1


## 📋 **Descrição do desafio e o meu passo a passo**  
Objetivo: este desafio tem como objetivo processar e gerar relatório de vendas, com foco em Linux e Markdown.

### Inicialmente, um arquivo (dados_de_vendas.csv) é disponibilizado, logo em seguida, deve ser criado um outro arquivo executavel chamado processamento_de_vendas.sh
![criaçao_processamento_de_vendas.sh](../evidencias/Criaçao_processo_de_vendas.png)



## O arquivo processamento_de_vendas.sh deve realizar as seguintes tarefas: 
### Criar um diretório "vendas"
### Copiar o arquivo dados_de_vendas.csv para dentro de vendas 
### Criar um diretório "backup" dentro de vendas
### Copiar o dados_de_vendas.csv para dentro do diretório backup com a data de execução como parte de seu nome
### Renomear o arquivo.csv dentro do diretório backup novamente, dessa vez deve ser adicionado a palavra "backup" para o nome do arquivo
### Criar no diretório backup um relatório.txt que contém:
    - data do sistema operacional
    - data do primeiro e do ultimo registro de vendas contido no arquivo.csv
    - quantidade total de itens diferentes vendidos no arquivo.csv
    - as primeiras 10 linhas do arquivo.csv
### Logo em seguida, o dados_de_vendas.csv deve ser compremido em um arquivo.zip no diretório backup, além disso, o dados_de_vendas.csv é excluido do diretório vendas 


![Conteúdo do processamento_de_vendas.sh](../evidencias/Processo_de_vendas.png)



## Depois disso, é preciso agendar a execução desse arquivo executavel(processamento_de_vendas.sh) por quatro dias, a execução deve ocorrer as 15 horas e 27 minutos, lembrando que, após cada execução, o arquivo.csv deve ter seus dados totalmente alterados manualmente
![Agendamento da execução do processamento_de_vendas.sh](../evidencias/Agendamento_Script.png)



## Após os quatro dias de execução, deve ser criado um outro arquivo executavel chamado consolidador_de_processamento_de_vendas.sh


## Esse consolidador_de_processamento_de_vendas.sh deve ter como função a junção dos quatro relatórios.txt gerados(referentes aos quatro dias de execução do script) em um novo relatório_final.txt, além disso, esse script deve ser executado manualmente

![Conteúdo do consolidador_de_processamento_de_vendas.sh](../evidencias/Consolidador_de_processo_de_vendas.png)



## Após a execução do script, esse é o resultado obtido, um novo relatorio_final.txt

![Gerando_relatorio_final](../evidencias/Relatorio_final.png)
