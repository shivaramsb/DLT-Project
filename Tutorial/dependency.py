import dlt
from pyspark.sql.functions import *

'''Creating an End To End Basic Pipeline'''

# Staging Area
@dlt.table(
    name = "Staging_orders"
)
def Staging_orders():
    df = spark.readStream.table("dlt.source.orders")
    return df

# Creating Transformed Area
@dlt.view(
    name = "transformed_orders"
)
def transformed_orders():
    df = spark.readStream.table("Staging_orders")
    df = df.withColumn("order_status", lower(col("order_status")))
    return df

# Creating Aggregated Area
@dlt.table(
    name = "aggregated_orders"
)
def aggregated_orders():
    df = spark.readStream.table("transformed_orders")
    df = df.groupBy("order_status").count()
    return df