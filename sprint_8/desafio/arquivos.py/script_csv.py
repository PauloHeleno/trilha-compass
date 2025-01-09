from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.transforms import *
from awsglue.dynamicframe import DynamicFrame
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import col, array_contains, split
import sys

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
sessao_Spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

caminho_csv = "s3://data-lake-do-paulo/Raw/Local/CSV/Movies/2024/12/13/" 
caminho_destino = "s3://data-lake-do-paulo/Trusted/CSV/" 

dados_brutos_dyf = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [caminho_csv]},
    format="csv",
    format_options={"withHeader": True, "separator": "|"}
)

meu_df = dados_brutos_dyf.toDF()

meu_df = meu_df.dropDuplicates()

meu_df = meu_df.replace("\\N", None)

meu_df_filtrado = meu_df.filter(
    col("genero").contains("Crime") | 
    col("genero").contains("Guerra")
)

meu_df_filtrado = meu_df_filtrado.coalesce(1) 

dados_refinados_trusted_dyf = DynamicFrame.fromDF(meu_df_filtrado, glueContext, "dados_processados")

glueContext.write_dynamic_frame.from_options(
    frame=dados_refinados_trusted_dyf,
    connection_type="s3",
    connection_options={"path": caminho_destino},
    format="parquet"
)

job.commit()
