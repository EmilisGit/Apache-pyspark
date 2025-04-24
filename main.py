from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("LocalApp").master("local[*]").getOrCreate()

data = [("Alice", 25), ("Bob", 30), ("Eve", 22)]
df = spark.createDataFrame(data, ["Name", "Age"])
df.show()
