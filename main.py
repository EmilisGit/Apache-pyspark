from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Lab2").master("local[*]").getOrCreate()
sc = spark.sparkContext

lines = sc.textFile("./data/duom_cut.txt")

lineLengths = lines.map(lambda s: len(s))
totalLength = lineLengths.reduce(lambda a, b: a + b)

print(f"Total lines: {totalLength}")