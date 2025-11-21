import asyncio
from fastapi import FastAPI, WebSocket
import random
import json
from datetime import datetime
from datetime import datetime, timedelta
app = FastAPI()

@app.websocket("/ws/websocket")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = generate_record()
        await websocket.send_text(json.dumps(data))
        await asyncio.sleep(1)
def generate_record():
    order_date = datetime.now() - timedelta(days=random.randint(0, 2000))
    shipping_date = order_date + timedelta(days=random.randint(1, 10))

    return {
        "Type": random.choice(["PAYMENT", "TRANSFER", "DEBIT", "CASH"]),
        "Days_for_shipping_real": random.randint(0, 10),
        "Days_for_shipment_scheduled": random.randint(1, 7),

        "Benefit_per_order": round(random.uniform(-300, 200), 2),
        "Sales_per_customer": round(random.uniform(20, 500), 2),

        "Delivery_Status": random.choice([
            "Late delivery", "Shipping on time",
            "Shipping canceled", "Advance shipping"
        ]),
        "Late_delivery_risk": random.randint(0, 1),

        "Customer_City": random.choice(["New York", "Paris", "Berlin", "Caguas", "Los Angeles"]),
        "Customer_Country": random.choice(["USA", "France", "Germany", "Puerto Rico"]),

        "Market": random.choice(["LATAM", "Europe", "Pacific Asia", "Africa", "USCA"]),

        "Order_City": random.choice(["Puebla", "Munich", "Shenzhen", "Tokyo"]),
        "Order_Country": random.choice(["México", "Alemania", "China", "Japón"]),

        "Order_Date": order_date.strftime("%Y-%m-%dT%H:%M:%S.000Z"),

        "Order_Item_Cardprod_Id": random.randint(100, 2000),
        "Order_Item_Discount": round(random.uniform(0, 50), 2),
        "Order_Item_Discount_Rate": round(random.uniform(0, 0.25), 2),

        "Order_Item_Product_Price": round(random.uniform(20, 400), 2),
        "Order_Item_Profit_Ratio": round(random.uniform(-2, 0.5), 2),

        "Order_Item_Quantity": random.randint(1, 5),
        "Sales": round(random.uniform(50, 500), 2),

        "Order_Item_Total": round(random.uniform(20, 500), 2),
        "Order_Profit_Per_Order": round(random.uniform(-200, 200), 2),

        "Order_Region": random.choice([
            "Central America", "Western Europe", "East of USA",
            "Northern Europe", "Oceania", "South America"
        ]),
        "Order_State": random.choice([
            "California", "Bavaria", "Tokyo", "Queensland", "Puebla"
        ]),
        "Order_Status": random.choice([
            "PENDING_PAYMENT", "PENDING", "COMPLETE",
            "SUSPECTED_FRAUD", "PROCESSING", "CLOSED"
        ]),

        "Product_Price": round(random.uniform(20, 400), 2),
        "Product_Status": random.choice([0, 1]),

        "Shipping_Date": shipping_date.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        "Shipping_Mode": random.choice(["Standard Class", "Second Class", "First Class", "Same Day"])
    }