import json
import requests
import boto3
import os

from datetime import datetime

def lambda_handler(event, context):
    api_key = os.environ['API_KEY']
    nome_bucket = "data-lake-do-paulo"
    linguagem = "pt-BR"
    limite_maximo_registros = 100

    id_genero_guerra = 10752
    id_genero_crime = 80 

    def pegar_filmes(url_base, filmes_por_pagina=20, paginas=10):
        filmes = []
        
        for pagina in range(1, paginas + 1):
            url = f"{url_base}&page={pagina}"
            resposta = requests.get(url).json()
            
            if 'results' in resposta:
                filmes.extend(resposta['results'])  
            else:
                break  
        
        return filmes

    filmes_guerra_url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language={linguagem}&with_genres={id_genero_guerra}"
    filmes_crime_url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language={linguagem}&with_genres={id_genero_crime}"

    filmes_guerra = pegar_filmes(filmes_guerra_url)
    filmes_crime = pegar_filmes(filmes_crime_url)


    detalhes_filmes_guerra = []

    detalhes_filmes_crime = []

   
    for filme in filmes_crime:
        id_filme = filme['id']
        url_detalhes = f"https://api.themoviedb.org/3/movie/{id_filme}?api_key={api_key}&language={linguagem}"
        url_informacoes = f"https://api.themoviedb.org/3/movie/{id_filme}/credits?api_key={api_key}&language={linguagem}"

        detalhes = requests.get(url_detalhes).json()
        informacoes = requests.get(url_informacoes).json()
        
        detalhes_filmes_crime.append({
            'Id': detalhes['id'],
            'Id no imdb': detalhes['imdb_id'],
            'Título': detalhes['title'],
            'Nota Média': detalhes['vote_average'],
            'Idioma Original': detalhes['original_language'],
            'Total de Votos': detalhes['vote_count'],
            'Data de Lançamento': detalhes['release_date'],
            'Popularidade': detalhes['popularity'],
            'Orçamento': detalhes['budget'],
            'Receita': detalhes['revenue'],
            'País de Produção': detalhes['production_countries'][0]['name'] if detalhes['production_countries'] else 'Não informado',
            'Adulto': detalhes['adult'],
            'Duração': detalhes['runtime'],
        })

    for filme in filmes_guerra:
        id_filme = filme['id']
        url_detalhes = f"https://api.themoviedb.org/3/movie/{id_filme}?api_key={api_key}&language={linguagem}"
        url_informacoes = f"https://api.themoviedb.org/3/movie/{id_filme}/credits?api_key={api_key}&language={linguagem}"

        detalhes = requests.get(url_detalhes).json()
        informacoes = requests.get(url_informacoes).json()
        
        detalhes_filmes_guerra.append({
            'Id': detalhes['id'],
            'Id no imdb': detalhes['imdb_id'],
            'Título': detalhes['title'],
            'Nota Média': detalhes['vote_average'],
            'Idioma Original': detalhes['original_language'],
            'Total de Votos': detalhes['vote_count'],
            'Data de Lançamento': detalhes['release_date'],
            'Popularidade': detalhes['popularity'],
            'Orçamento': detalhes['budget'],
            'Receita': detalhes['revenue'],
            'País de Produção': detalhes['production_countries'][0]['name'] if detalhes['production_countries'] else 'Não informado',
            'Adulto': detalhes['adult'],
            'Duração': detalhes['runtime'],
        })


    s3_client = boto3.client('s3')

    hoje = datetime.today()
    ano = hoje.strftime('%Y')
    mes = hoje.strftime('%m')
    dia = hoje.strftime('%d')


    for i in range(0, len(detalhes_filmes_guerra), limite_maximo_registros):
        parte = detalhes_filmes_guerra[i:i + limite_maximo_registros]
        nome_arquivo = f"filmes_aguerra.json"
        s3_path = f"Raw/TMDB/JSON/{ano}/{mes}/{dia}/{nome_arquivo}"
        conteudo_arquivo = json.dumps(parte, indent=4, ensure_ascii=False)
        s3_client.put_object(Bucket=nome_bucket, Key=s3_path, Body=conteudo_arquivo)

    for i in range(0, len(detalhes_filmes_crime), limite_maximo_registros):
        parte = detalhes_filmes_crime[i:i + limite_maximo_registros]
        nome_arquivo = f"filmes_crime.json"
        s3_path = f"Raw/TMDB/JSON/{ano}/{mes}/{dia}/{nome_arquivo}"
        conteudo_arquivo = json.dumps(parte, indent=4, ensure_ascii=False)
        s3_client.put_object(Bucket=nome_bucket, Key=s3_path, Body=conteudo_arquivo)


    return {
        'statusCode': 200,
        'body': json.dumps("Arquivos gerados e enviados ao S3 com sucesso!")
    }
