import asyncio
import websockets
import pickle
import json
import socket

HOST = '192.168.50.161'  # The socket server's hostname or IP address
PORT = 65431        # The port used by the server
Gateway_IP = '127.0.0.1'  # for websocket server

data = ''
connect = 0

print('start')

async def hello(websocket, path):
    global data, connect
    while True:
        if connect != 0:
            data = conn.recv(1024).decode('utf-8')
            print('Received from socket server : ', data)
            line = await websocket.recv()
            print(data)
            if line is None:
                return
            await websocket.send(data)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
print('accept finish')
with conn:
    print('sdsdsd')
    connect = conn
    start_server = websockets.serve(hello, Gateway_IP, 8866)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
