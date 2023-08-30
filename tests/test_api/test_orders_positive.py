import pytest
import requests

def test_get_orders(base_url):
    response = requests.get(f"{base_url}/orders")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    

def test_place_order(base_url):
    order_data = {"stoks": "AAPL", "quantity": 10}
    response = requests.post(f"{base_url}/orders", json=order_data)
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["status"] == "pending"
    

def test_get_order(base_url):
    response = requests.get(f"{base_url}/orders/1")
    assert response.status_code == 200
    assert "id" in response.json()
    

def test_cancel_order(base_url):
    response = requests.delete(f"{base_url}/orders/1")
    assert response.status_code == 204
    response = requests.get(f"{base_url}/orders/1")
    assert response.json()["status"] == "cancelled"
    
