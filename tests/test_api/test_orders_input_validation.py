import pytest
import requests

def test_place_order_invalid_inputs(base_url):
    order_data = {"stoks": "", "quantity": -1}
    response = requests.post(f"{base_url}/orders", json=order_data)
    assert response.status_code == 400
    assert response.json() == {"code": 400, "message": "Invalid Input"}

def test_place_order_one_invalid_input(base_url):
    order_data = {"stoks": "", "quantity": 100}
    response = requests.post(f"{base_url}/orders", json=order_data)
    assert response.status_code == 400
    assert response.json() == {"code": 400, "message": "Invalid Input"}

def test_place_order_one_invalid_input_name(base_url):
    order_data = {"stocks": "USDGBP", "quantity": 30}
    response = requests.post(f"{base_url}/orders", json=order_data)
    assert response.status_code == 400
    assert response.json() == {"code": 400, "message": "Invalid Input"}

def test_place_order_invalid_input_names(base_url):
    order_data = {"stocks": "JYPGBP", "quantities": 30}
    response = requests.post(f"{base_url}/orders", json=order_data)
    assert response.status_code == 400
    assert response.json() == {"code": 400, "message": "Invalid Input"}

def test_get_order_stringid(base_url):
    id = "one"
    response=requests.get(f"{base_url}/orders/{id}")
    assert response.status_code == 400
    assert response.json() == {"code": 400, "message": "Invalid Input"}

def test_cancel_order_stringid(base_url):
    id = "one"
    response=requests.delete(f"{base_url}/orders/{id}")
    assert response.status_code == 400
    assert response.json() == {"code": 400, "message": "Invalid Input"}