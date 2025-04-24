from pyspark.sql import SparkSession
from Helpers import Helpers
import re

spark = SparkSession.builder.appName("Lab2").master("local[*]").getOrCreate()
sc = spark.sparkContext

lines = sc.textFile("./data/duom_cut.txt")
entries = lines.flatMap(lambda line: list(Helpers.extract_entries(line, ["svoris", "svorio grupe"])))

group_weight_pairs = entries.map(lambda entry: (entry["svorio grupe"], entry["svoris"]))

grouped_rdd = group_weight_pairs.groupByKey()

result = grouped_rdd.mapValues(lambda weights: (min(weights), max(weights)))

# Format the results
formatted_results = result.map(lambda x: {
    "weight_group": x[0],
    "min_weight": x[1][0],
    "max_weight": x[1][1]
})

# Collect and print the results
results = formatted_results.collect()
for result in results:
    print(f"Weight Group: {result['weight_group']}, Min Weight: {result['min_weight']}, Max Weight: {result['max_weight']}")