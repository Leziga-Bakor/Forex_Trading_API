import asyncio
import random
import json
from fastapi import WebSocket
from fastapi.websockets import WebSocketDisconnect
from app.api.models.order import OrderInput
from app.api.endpoints.orders import create_order


class WebSocketManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        """
        Establish a WebSocket connection with a client.

        Args:
            websocket (WebSocket): The WebSocket object representing the client connection.

        """
        await websocket.accept()
        self.active_connections.append(websocket)
        try:
            while True:
                data = await websocket.receive_text()
                data = json.loads(data)
                await self.process_order(websocket, data)
        except WebSocketDisconnect:
            self.active_connections.remove(websocket)

    async def process_order(self, websocket: WebSocket, data: dict):  
        """
        Process an incoming order request, create an order, and send a response.

        Args:
            websocket (WebSocket): The WebSocket object representing the client connection.
            data (dict): The order data received from the client.

        """     
        order_data=OrderInput(stoks=data["stoks"], quantity=data["quantity"])
        order = await create_order(order_data)
        response_data = {
            "orderId": order.id,
            "orderStatus": order.status
        }
        await websocket.send_json(response_data)
        order_status = await self.simulate_order_status()
        await self.notify_subscribers(order.id, order_status)

    async def simulate_order_status(self):
        """
        Simulate order status changes with a random delay.

        Returns:
            str: A randomly selected order status ("executed" or "cancelled").
        """
        await asyncio.sleep(random.uniform(0.1, 0.5))
        return random.choice(["executed", "cancelled"])

    async def notify_subscribers(self, order_id, order_status):
        """
        Notify subscribers of order status updates.

        Args:
            order_id (str): The ID of the order.
            order_status (str): The updated order status.
        """
        for connection in self.active_connections:
            try:
                await connection.send_json({"notification": f"Order {order_id} {order_status}"})
            except Exception:
                pass

websocket_manager = WebSocketManager()
