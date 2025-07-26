from pyspark.sql import SparkSession
from config.load_config import load_config_from_key_vault

config = load_config_from_key_vault()

if config is None:
    raise Exception("Failed to load configuration from Azure Key Vault")

spark = SparkSession.builder.getOrCreate()

# loads CSV from aazure Blob Storage using WASBS protocol
spark.conf.set("fs.azure.account.key.premmystoragev201.dfs.core.windows.net", config ["storage_key"])

df = spark.read.csv("wasbs://premmycontainer@premmystoragev201.blob.core.windows.net/patients_data.csv", header=True)

#print schema
df.printSchema()
df.show(5)

#save to delta lake in mounted path
df.write.format("delta").mode("overwrite").save("/mnt/datalake/my_csv_as_delta")


