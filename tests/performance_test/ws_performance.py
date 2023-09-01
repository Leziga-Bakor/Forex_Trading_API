import json
import asyncio
import websockets
import statistics
import time

order_data = {
    "stoks": "CADUSD",
    "quantity": 10
}

ws_url = "ws://localhost:8080/ws"

ws_timestamps = []

async def websocket_task():
    """ Function to call websocket and get times for start and end"""
    async with websockets.connect(ws_url) as websocket:
        try:
            await websocket.send(json.dumps(order_data))
            start_time = time.time()  
            await websocket.recv()
            response = await websocket.recv()
            end_time = time.time()  
            ws_timestamps.append((start_time, end_time))  
        except Exception as e:
            print(f"WebSocket Error: {str(e)}")

num_ws_requests = 100

loop = asyncio.get_event_loop()
ws_tasks = [loop.create_task(websocket_task()) for _ in range(num_ws_requests)]
loop.run_until_complete(asyncio.wait(ws_tasks))

# Calculate average execution delay and standard deviation for WebSocket notifications
ws_delays = [(b - a) for a, b in ws_timestamps]
ws_average_delay = round(sum(ws_delays) / num_ws_requests,3)
ws_std_deviation = round(statistics.stdev(ws_delays),3)

print(f"WebSocket Average Execution Delay: {ws_average_delay} seconds")
print(f"WebSocket Standard Deviation: {ws_std_deviation} seconds")