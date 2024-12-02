import boto3
import pandas as pd
from io import StringIO

session = boto3.Session(profile_name='Paulo')
s3_cliente = session.client('s3')

bucket_name = "bucket-desafio.com"
s3_key = "producao-mar-2024.csv"

try:
    response = s3_cliente.get_object(Bucket=bucket_name, Key=s3_key)
    csv_content = response['Body'].read().decode('utf-8')
    df = pd.read_csv(StringIO(csv_content))
    print("Arquivo carregado com sucesso do S3.")
except Exception as e:
    print(f"Erro ao carregar o arquivo do S3: {e}")
    exit()

meses_portugues_para_ingles = {
    'jan': 'Jan', 'fev': 'Feb', 'mar': 'Mar', 'abr': 'Apr', 'mai': 'May', 'jun': 'Jun',
    'jul': 'Jul', 'ago': 'Aug', 'set': 'Sep', 'out': 'Oct', 'nov': 'Nov', 'dez': 'Dec'
}

df = df[(df['[Estado]'] == 'Rio de Janeiro') & (df['[Produção de Óleo (m³)]'] > 0)]

df['[Produção Total (m³)]'] = (
    df['[Produção de Óleo (m³)]'] + df['[Produção de Água (m³)]']
)

df['[Gás Total (Mm³)]'] = (
    df['[Produção de Gás Associado (Mm³)]'] + df['[Produção de Gás Não Associado (Mm³)]']
)

df_condicional = df[df['[Produção de Gás Não Associado (Mm³)]'] > 0]

df['[Produção de óleo (Mm³)]'] = df['[Produção de Óleo (m³)]'] / 1e3

df[['Mês', 'Ano']] = df['[Mês/Ano]'].str.split('/', expand=True)
df['Mês'] = df['Mês'].str.lower().replace(meses_portugues_para_ingles)
df['Data'] = pd.to_datetime(df['Ano'] + '-' + df['Mês'], format='%Y-%b')
df['[Poço]'] = df['[Poço]'].str.upper()

csv_filename = "dados_processados.csv"
df.to_csv(csv_filename, index=False)
print(f"Arquivo {csv_filename} salvo com sucesso.")

s3_key_processed = "dados_processados.csv"

try:
    s3_cliente.upload_file(csv_filename, bucket_name, s3_key_processed)
    print(f"Arquivo enviado para o bucket {bucket_name} com a chave {s3_key_processed}.")
except Exception as e:
    print(f"Erro ao enviar o arquivo para o S3: {e}")
