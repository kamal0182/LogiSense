from sqlalchemy import (
    Table, Column, Integer, String, Float,
    MetaData, DateTime, create_engine
)
try  : 
    engine = create_engine('postgresql://postgres:kamal1234@localhost:5432/Logistics_Management_System_db')
    print("connected Succes")
except ValueError : 
    print(ValueError)
metadata = MetaData()


orders_table = Table(
    "orders", metadata,

    Column("id", Integer, primary_key=True),

    Column("Type", String(50)),
    Column("Days_for_shipping_real", Integer),
    Column("Days_for_shipment_scheduled", Integer),
    Column("Benefit_per_order", Float),
    Column("Sales_per_customer", Float),
    Column("Delivery_Status", String(50)),
    Column("Late_delivery_risk", Integer),
    Column("Customer_City", String(100)),
    Column("Customer_Country", String(100)),
    Column("Market", String(100)),
    Column("Order_City", String(100)),
    Column("Order_Country", String(100)),
    Column("Order_Date", DateTime),
    Column("Order_Item_Cardprod_Id", Integer),
    Column("Order_Item_Discount", Float),
    Column("Order_Item_Discount_Rate", Float),
    Column("Order_Item_Product_Price", Float),
    Column("Order_Item_Profit_Ratio", Float),
    Column("Order_Item_Quantity", Integer),
    Column("Sales", Float),
    Column("Order_Item_Total", Float),
    Column("Order_Profit_Per_Order", Float),
    Column("Order_Region", String(100)),
    Column("Order_State", String(100)),
    Column("Order_Status", String(50)),
    Column("Product_Price", Float),
    Column("Product_Status", Integer),
    Column("Shipping_Date", DateTime),
    Column("Shipping_Mode", String(50)),
)
metadata.create_all(engine)
print("created")





