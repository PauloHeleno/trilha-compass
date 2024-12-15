import boto3
from botocore.exceptions import ClientError
import os
from datetime import datetime

def criar_bucket(bucket_nome, region="us-east-1"):
    try:
        session = boto3.Session(profile_name='Paulo')
        s3_cliente = session.client('s3', region_name=region)

        if region == "us-east-1":
            s3_cliente.create_bucket(Bucket=bucket_nome)
        else:
            s3_cliente.create_bucket(
                Bucket=bucket_nome,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print(f"O bucket '{bucket_nome}' foi criado com sucesso na região '{region}'.")
    except ClientError as erro:
        if erro.response['Error']['Code'] == 'BucketAlreadyExists':
            print(f"Erro: O bucket '{bucket_nome}' já existe globalmente e pertence a outra conta.")
        else:
            print(f"Erro ao criar o bucket: {erro}")

def enviar_arquivo_s3(bucket_nome, arquivo_local, origem, formato, especificacao, camada):
    try:
        session = boto3.Session(profile_name='Paulo')
        s3_cliente = session.client('s3')

        data_atual = datetime.now()
        nome_arquivo = os.path.basename(arquivo_local) 
        caminho_s3 = f"{camada}/{origem}/{formato}/{especificacao}/{data_atual.year}/{data_atual.month:02d}/{data_atual.day:02d}/{nome_arquivo}"
        
        
        s3_cliente.upload_file(arquivo_local, bucket_nome, caminho_s3)
        print(f"Arquivo '{nome_arquivo}' enviado para '{caminho_s3}' no bucket '{bucket_nome}'.")
    except ClientError as erro:
        print(f"Erro ao enviar o arquivo: {erro}")

bucket = "data-lake-do-paulo"
region = "us-east-1"

criar_bucket(bucket, region)

arquivos = [
    {"arquivo": r"/app/csv/movies.csv", "origem": "Local", "formato": "CSV", "especificacao": "Movies", "camada": "Raw"},
    {"arquivo": r"/app/csv/series.csv", "origem": "Local", "formato": "CSV", "especificacao": "Series", "camada": "Raw"},
]



for item in arquivos:
    enviar_arquivo_s3(bucket, item["arquivo"], item["origem"], item["formato"], item["especificacao"], item["camada"])
