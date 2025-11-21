import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType

# def foreach_batch_function(df, epoch_id):
#     df.format("jdbc").option("url", "url")\
#       .option("dbtable","test").option("user","postgres")\
#       .option("password", "password").save()
# df5.writeStream.foreachBatch(foreach_batch_function).start()   

def start_streaming(driver):
    stream_df = (driver.readStream
                 .format("socket")
                 .option("host", "127.0.0.1")
                 .option("port", 9999)
                 .option("url", "jdbc:postgresql://localhost:5432/")
                 .load()
    )
    # df = (spark.read 
    # .format("jdbc") 
    # .option("url", "jdbc:postgresql://localhost:5432/mydb") 
    # .option("dbtable", "public.orders") 
    # .option("user", "postgres") 
    # .option("password", "kamal1234") 
    # .option("driver", "org.postgresql.Driver") 
    # .load() )

    schema = StructType([
    StructField("Type", StringType(), True),
    StructField("Days_for_shipping_real", IntegerType(), True),
    StructField("Days_for_shipment_scheduled", IntegerType(), True),
    StructField("Benefit_per_order", DoubleType(), True),
    StructField("Sales_per_customer", DoubleType(), True),
    StructField("Delivery_Status", StringType(), True),
    StructField("Late_delivery_risk", IntegerType(), True),
    StructField("Customer_City", StringType(), True),
    StructField("Customer_Country", StringType(), True),
    StructField("Market", StringType(), True),
    StructField("Order_City", StringType(), True),
    StructField("Order_Country", StringType(), True),
    StructField("Order_Date", StringType(), True),   # You can change to TimestampType if needed
    StructField("Order_Item_Cardprod_Id", IntegerType(), True),
    StructField("Order_Item_Discount", DoubleType(), True),
    StructField("Order_Item_Discount_Rate", DoubleType(), True),
    StructField("Order_Item_Product_Price", DoubleType(), True),
    StructField("Order_Item_Profit_Ratio", DoubleType(), True),
    StructField("Order_Item_Quantity", IntegerType(), True),
    StructField("Sales", DoubleType(), True),
    StructField("Order_Item_Total", DoubleType(), True),
    StructField("Order_Profit_Per_Order", DoubleType(), True),
    StructField("Order_Region", StringType(), True),
    StructField("Order_State", StringType(), True),
    StructField("Order_Status", StringType(), True),
    StructField("Product_Price", DoubleType(), True),
    StructField("Product_Status", IntegerType(), True),
    StructField("Shipping_Date", StringType(), True),  # Or TimestampType
    StructField("Shipping_Mode", StringType(), True)
])

    json_df = stream_df.select(from_json(col("value"), schema).alias("data")).select("data.*")

    query = json_df.writeStream.outputMode("append").format("console").start()
    query.awaitTermination()

import os
os.environ["JAVA_HOME"] = "C:\\Program Files\\Java\\jdk-17"
os.environ["PATH"] = os.environ["JAVA_HOME"] + "\\bin;" + os.environ["PATH"]


os.environ["PYSPARK_PYTHON"] = r"C:\Users\kamal\AppData\Local\Programs\Python\Python310\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:\Users\kamal\AppData\Local\Programs\Python\Python310\python.exe"
os.environ["HADOOP_HOME"] = r"C:\\hadoop"
os.environ["PATH"] = os.environ["HADOOP_HOME"] + r"\bin;" + os.environ["PATH"]

from pyspark.sql import SparkSession
if __name__ == "__main__":
    driver = spark = SparkSession.builder.appName("congig").master("local[*]").config("spark.driver.memory", "8g").getOrCreate()
    start_streaming(driver)
