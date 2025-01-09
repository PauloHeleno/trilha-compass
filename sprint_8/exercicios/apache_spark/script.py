from pyspark.sql import SparkSession
from pyspark.sql.functions import rand, when, floor, col
from pyspark import SparkContext, SQLContext


# etapa 1

spark = SparkSession \
    .builder \
    .master ("local[*]") \
    .appName("Exercicio Intro") \
    .getOrCreate()


df_nomes = spark.read.csv(
    "nomes_aleatorios.txt",  
    header=False,               
    inferSchema=True                    
)

df_nomes.show(5)

# etapa 2
df_nomes = df_nomes.withColumnRenamed("_c0", "nomes")

df_nomes.printSchema()

df_nomes.show(10)

# etapa 3

df_nomes = df_nomes.withColumn(
    "Escolaridade",
    when(rand() < 0.33, "Fundamental") 
    .when(rand() < 0.66, "Medio")      
    .otherwise("Superior")             
)

df_nomes.show(10)


# etapa 4

paises = [
    "Brasil", "Argentina", "Uruguai", "Chile", "Paraguai", 
    "Colombia","Venezuela", "Equador", "Peru", "Bolivia", 
    "Guiana", "Suriname", "Guiana Francesa"
]

df_nomes = df_nomes.withColumn(
    "Pais",
    when(rand() < 1/len(paises), paises[0])  
    .when(rand() < 2/len(paises), paises[1])  
    .when(rand() < 3/len(paises), paises[2])  
    .when(rand() < 4/len(paises), paises[3])
    .when(rand() < 5/len(paises), paises[4])
    .when(rand() < 6/len(paises), paises[5])
    .when(rand() < 7/len(paises), paises[6])
    .when(rand() < 8/len(paises), paises[7])
    .when(rand() < 9/len(paises), paises[8])
    .when(rand() < 10/len(paises), paises[9])
    .when(rand() < 11/len(paises), paises[10])
    .when(rand() < 12/len(paises), paises[11])
    .otherwise(paises[12])
)

df_nomes.show(10)

# etapa 5

df_nomes = df_nomes.withColumn(
    "anoNascimento",
    floor(rand() * 66 + 1945)
)

df_nomes.show(10)


# etapa 6

df_select = df_nomes.filter(col("anoNascimento") >= 2000).select(
    "nomes",  
    when(col("anoNascimento") >= 2000, "Nasceu nesse seculo")
    .otherwise("Nascido antes de 2000").alias("categoria") 
)

df_select.show(10)


# etapa 7

df_nomes.createOrReplaceTempView("pessoas")

spark.sql("SELECT * FROM pessoas WHERE anoNascimento >= 2000").show(10)


# etapa 8

df_contagem = df_nomes.filter((col("anoNascimento") >= 1980) & (col("anoNascimento") <= 1994)).count()

print(f"Total: {df_contagem}")


# etapa 9



resultado = spark.sql("SELECT COUNT(*) as total FROM pessoas WHERE anoNascimento BETWEEN 1980 AND 1994")

resultado.show()


# etapa 10

df_resultado = spark.sql("""
SELECT 
    pais,
    CASE 
        WHEN anoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
        WHEN anoNascimento BETWEEN 1965 AND 1979 THEN 'Geracoo X'
        WHEN anoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
        WHEN anoNascimento BETWEEN 1995 AND 2015 THEN 'Geracao Z'
    END AS geracao,
    COUNT(*) AS quantidade
FROM pessoas
GROUP BY pais, geracao
ORDER BY pais ASC, geracao ASC, quantidade ASC
""")

df_resultado.show(10)

