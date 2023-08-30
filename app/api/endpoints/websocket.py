import asyncio
import random
from fastapi import WebSocket
from fastapi.exceptions import WebSocketDisconnect
from app.api.endpoints.orders import create_order
from app.api.models.order import OrderInput

class WebSocketManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        try:
            while True:
                data = await websocket.receive_text()
                await self.process_order(websocket, data)
        except WebSocketDisconnect:
            self.active_connections.remove(websocket)

    async def process_order(self, websocket: WebSocket, data: dict):
        order = await create_order(OrderInput(**data))
        response_data = {
            "orderId": order.id,
            "orderStatus": order.status
        }
        await websocket.send_json(response_data)
        order_status = await self.simulate_order_status()
        await self.notify_subscribers(order.id, order_status)

    async def simulate_order_status(self):
        await asyncio.sleep(random.uniform(0.1, 0.5))
        return random.choice(["executed", "cancelled"])

    async def notify_subscribers(self, order_id, order_status):
        for connection in self.active_connections:
            try:
                await connection.send_json({"notification": f"Order {order_id} {order_status}"})
            except Exception:
                pass

websocket_manager = WebSocketManager()
