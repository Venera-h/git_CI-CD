import pytest
from fastapi.testclient import TestClient
from main import app, CART, ORDERS

client = TestClient(app)

def test_health():
    """Проверка endpoint /health"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_products():
    """Проверка endpoint /products"""
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_search():
    """Проверка endpoint /search"""
    response = client.get("/search?q=nvidia")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_cart_empty():
    """Проверка пустой корзины"""
    CART.clear()
    response = client.get("/cart")
    assert response.status_code == 200
    assert response.json()["total"] == 0

def test_cart_add():
    """Проверка добавления товара в корзину"""
    CART.clear()
    response = client.post("/cart/add?pid=0&qty=2")
    assert response.status_code == 200
    assert response.json()["ok"]

def test_cart_add_invalid():
    """Проверка добавления несуществующего товара"""
    response = client.post("/cart/add?pid=999")
    assert response.status_code == 404

def test_clear_cart():
    """Проверка очистки корзины"""
    response = client.delete("/cart")
    assert response.status_code == 200
    assert response.json()["ok"]

def test_checkout():
    """Проверка оформления заказа"""
    CART.clear()
    ORDERS.clear()
    client.post("/cart/add?pid=0&qty=1")
    response = client.post("/checkout")
    assert response.status_code == 200
    assert "id" in response.json()

def test_checkout_empty_cart():
    """Проверка оформления заказа с пустой корзиной"""
    CART.clear()
    response = client.post("/checkout")
    assert response.status_code == 400

def test_orders():
    """Проверка получения списка заказов"""
    response = client.get("/orders")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
