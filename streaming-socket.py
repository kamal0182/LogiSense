import asyncio
import websockets
import socket

HOST, PORT = "127.0.0.1", 9999
WS_URI = "ws://127.0.0.1:8000/ws/websocket"

async def websocket_to_tcp():
    # Create TCP server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"TCP Server listening on {HOST}:{PORT} ...")
    conn, addr = s.accept()
    print(f"TCP client connected: {addr}")

    # Connect to WebSocket
    async with websockets.connect(WS_URI) as ws:
        print(f"Connected to WebSocket {WS_URI}")
        try:
            while True:
                data = await ws.recv()           # already a JSON string
                conn.send(data.encode("utf-8") + b"\n")  # send to TCP
                print(f"Sent: {data}")
        except (BrokenPipeError, ConnectionResetError):
            print("TCP client disconnected")
        finally:
            conn.close()
if __name__ == "__main__":
    asyncio.run(websocket_to_tcp())
