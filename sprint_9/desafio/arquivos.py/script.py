from pyspark.context import SparkContext
from pyspark.sql.functions import col, current_date, date_format
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from awsglue.utils import getResolvedOptions
from datetime import datetime
import sys

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

caminho_local = "s3://data-lake-do-paulo/Trusted/LOCAL/PARQUET/MOVIES/"
caminho_tmdb = "s3://data-lake-do-paulo/Trusted/TMDB/PARQUET/MOVIES/2024/12/30"

parquet_local = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [caminho_local]},
    format="parquet"
)

parquet_tmdb = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [caminho_tmdb]},
    format="parquet"
)

df_tmdb = parquet_tmdb.toDF()
df_local = parquet_local.toDF()

df_local = df_local.withColumnRenamed("id", "id_local")

df_unido = df_tmdb.join(
    df_local,
    (df_tmdb["id_no_imdb"] == df_local["id_local"]) & 
    (df_tmdb["Orçamento"].isNotNull()) & 
    (df_tmdb["Receita"].isNotNull()),
    "inner"
)

df_unido = df_unido.withColumn("lucro", col("Receita") - col("Orçamento"))

df_fato = df_unido.select(
    col("id_local").alias("id_fato"), col("id_no_imdb").alias("id_filme"),
    col("lucro"), col("Receita"), col("Orçamento"),
    col("Popularidade"), col("nota_média"), col("total_de_votos")
).dropDuplicates()

df_dim_filme = df_unido.select(
    col("id_no_imdb").alias("id_filme"),  
    col("Título"), col("tituloOriginal"),
    col("anoLancamento"), col("Duração"),
    col("Adulto"), col("país_de_produção")
).dropDuplicates()

df_fato = df_fato.coalesce(1)
df_dim_filme = df_dim_filme.coalesce(1)

hoje = datetime.today()
ano = hoje.strftime('%Y')
mes = hoje.strftime('%m')
dia = hoje.strftime('%d')

caminho_fato = f"s3://data-lake-do-paulo/Refined/PARQUET/FATO/{ano}/{mes}/{dia}/"
caminho_dim_filme = f"s3://data-lake-do-paulo/Refined/PARQUET/DIM_FILME/{ano}/{mes}/{dia}/"

fato_dyf = DynamicFrame.fromDF(df_fato, glueContext, "fato_dyf")
glueContext.write_dynamic_frame.from_options(
    frame=fato_dyf,
    connection_type="s3",
    connection_options={"path": caminho_fato},
    format="parquet"
)

dim_filme_dyf = DynamicFrame.fromDF(df_dim_filme, glueContext, "dim_filme_dyf")
glueContext.write_dynamic_frame.from_options(
    frame=dim_filme_dyf,
    connection_type="s3",
    connection_options={"path": caminho_dim_filme},
    format="parquet"
)

job.commit()
