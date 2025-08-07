import dlt 

# Creating Streaming Table
@dlt.table(
    name = "First_stream_table"
)
def First_stream_table():
    df = spark.readStream.table("dlt.source.orders")
    return df

#Creating Materalized View
@dlt.table(
    name = "First_mat_view"
)
def First_mat_view():
    df = spark.read.table("dlt.source.orders")
    return df

# Creating Batch View
@dlt.view(
    name = "First_batch_view"
)
def First_batch_view():
    df = spark.read.table("dlt.source.orders")
    return df

# Creating Streaming View
@dlt.view(
    name = "First_stream_view"
)
def First_stream_view():
    df = spark.readStream.table("dlt.source.orders")
    return df