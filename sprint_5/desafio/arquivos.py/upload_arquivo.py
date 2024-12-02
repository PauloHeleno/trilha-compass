import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def upload_para_bucket(nome_arquivo, nome_bucket, nome_objeto=None):
    if nome_objeto is None:
        nome_objeto = nome_arquivo.split('/')[-1]
    
    try:
        session = boto3.Session(profile_name='Paulo')
        s3_cliente = session.client('s3')
        
        s3_cliente.upload_file(nome_arquivo, nome_bucket, nome_objeto)
        print(f"Arquivo '{nome_arquivo}' enviado com sucesso para 's3://{nome_bucket}/{nome_objeto}'.")
    except FileNotFoundError:
        print("Erro: O arquivo especificado não foi encontrado.")
    except NoCredentialsError:
        print("Erro: Credenciais AWS não foram encontradas.")
    except PartialCredentialsError:
        print("Erro: As credenciais AWS estão incompletas.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

caminho_arquivo = r"producao-mar-2024.csv"
bucket = "bucket-desafio.com"

upload_para_bucket(caminho_arquivo, bucket)
