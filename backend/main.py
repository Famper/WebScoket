import asyncio
import websockets
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)

async def handler(websocket, path):
    logging.info("Client connected")
    try:
        async for message in websocket:
            logging.info(f"Received message: {message}")
            response = f"Echo: {message}"
            await websocket.send(response)
    except websockets.exceptions.ConnectionClosed:
        logging.info("Client disconnected")

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        logging.info("WebSocket server started on ws://0.0.0.0:8765")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
