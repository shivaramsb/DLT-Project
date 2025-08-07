import dlt

# Products_Expections
products_rules = {
    "rule_1" : "product_id IS NOT NULL",
    "rule_2" : "price >=0"
}

# Ingesting Products
@dlt.table(
    name= "products_stg"
)
@dlt.expect_all_or_drop(products_rules)
def products_stg():

    df = spark.readStream.table("dlt.source.products")
    return df