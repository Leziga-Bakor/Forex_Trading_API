import pytest
import json
import websockets

@pytest.mark.asyncio
async def test_websocket_order_processing(base_url):
    async with websockets.connect(f"{base_url}") as websocket:
        order_data = {
            "stoks": "GBPUSD",
            "quantity": 22
        }
        await websocket.send(json.dumps(order_data))
        
        response_data = await websocket.recv()
        response_json = json.loads(response_data)
        
        assert "orderId" in response_json
        assert "orderStatus" in response_json

@pytest.mark.asyncio
async def test_websocket_notification(base_url):
    async with websockets.connect(f"{base_url}") as websocket1:
        async with websockets.connect(f"{base_url}") as websocket2:
            order_data = {
                "stoks": "JYPCHF",
                "quantity": 40
            }
            await websocket1.send(json.dumps(order_data))
            await websocket1.recv()  
            
            notification_data = await websocket1.recv()
            notification_json = json.loads(notification_data)
            
            assert "notification" in notification_json

            notification_data = await websocket2.recv()
            notification_json = json.loads(notification_data)
            
            assert "notification" in notification_json
