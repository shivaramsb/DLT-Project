import dlt

# Sales Expectatios
sales_rules = {
    "rule_1" : "sales_id IS NOT NULL"
}

# Creating Empty streaming Table
dlt.create_streaming_table(
    name = "sales_stg",
    expect_all_or_drop = sales_rules 
)

# Creating East Sales Flow
@dlt.append_flow(target = "sales_stg")
def east_sales():
    df = spark.readStream.table("dlt.source.sales_east")
    return df


# Creating West Sales Flow
@dlt.append_flow(target = "sales_stg")
def west_sales():
    df = spark.readStream.table("dlt.source.sales_west")
    return df