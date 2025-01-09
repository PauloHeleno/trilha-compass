from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import col, to_date, when
import sys

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

caminho_json = "s3://data-lake-do-paulo/Raw/TMDB/JSON/2024/12/30/" 
caminho_destino = "s3://data-lake-do-paulo/Trusted/JSON/2024/12/30/"

dados_brutos_dyf = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [caminho_json]},
    format="json"
)


df = dados_brutos_dyf.toDF()

df = df.dropDuplicates()

df = df.withColumn("Data de Lançamento", to_date(col("Data de Lançamento"), "yyyy-MM-dd"))

df = df.withColumn("Orçamento", when(col("Orçamento") == 0, None).otherwise(col("Orçamento")))
df = df.withColumn("Receita", when(col("Receita") == 0, None).otherwise(col("Receita")))

df = df.coalesce(1) 

dados_refinados_dyf = DynamicFrame.fromDF(df, glueContext, "dados_refinados")

glueContext.write_dynamic_frame.from_options(
    frame=dados_refinados_dyf,
    connection_type="s3",
    connection_options={"path": caminho_destino},
    format="parquet"
)

job.commit()
