from pyspark.sql import SparkSession

jsonFormatSchema = open("data/avro_utils/person.avsc", "r").read()

spark = SparkSession \
    .builder \
    .appName("myapp") \
    .config('spark.jars', 'jars/spark-avro_2.12-3.1.2.jar') \
    .getOrCreate()

# ***** Part 1 - Compaction *************
# Using the Spark API, write code to generate a SINGLE Avro file that will contain all the records
# of the three input files in the ./data/input directory.
# You can output this file to the path of your choice on your local machine.
# ***************************************

# ***** Part 2 - Partitioning ***********
# Using the result of the first step, write the code to generate the data again, but this time partitioned by age,
# excluding people that are younger than 21. Output should look like :
# \path\age=21\***.avro
# \path\age=24\***.avro
# ***************************************

# ***** Question 1 **********************
# Can you explain why compaction can be necessary in datalakes?
# Please write the answer in a few sentences as a comment in the lines below.
# ***************************************

# ***** Question 2 **********************
# Explain whether avro files are a good choice of file format for a datalake.
# Please write the answer in a few sentences as a comment in the lines below.
# ***************************************


