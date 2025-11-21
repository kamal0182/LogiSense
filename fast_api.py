# from fastapi import FastAPI, WebSocket
# import asyncio
# import random

# app = FastAPI()
# people = [{"id":1,"name":"Adam","age":24}, {"id":2,"name":"Sara","age":29}]

# @app.websocket("/stream")
# async def websocket_endpoint(ws: WebSocket):
#     await ws.accept()
#     while True:
#         await ws.send_json(random.choice(people))
#         await asyncio.sleep(
