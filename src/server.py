# server.py

# description

# import statements
import asyncio
from websockets.asyncio.server import serve

async def handler(websocket):
    while True:
        message = await websocket.recv()
        print(message)

async def main():
    async with serve(handler, "localhost", 8765):
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())