import pytest
import requests
from api_client import create_order
from helpers import get_order_payload
import allure

@allure.epic("Создание заказа")
@allure.feature("API /api/v1/orders")
class TestCreateOrders:

    @allure.title("Создание заказа с цветом: {color}")
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order_with_colors(self, color):
        payload = get_order_payload(color)
        response = create_order(payload)
        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title("Проверка наличия track в ответе")
    def test_create_order_returns_track(self):
        payload = get_order_payload(["BLACK"])
        response = create_order(payload)
        assert response.status_code == 201

        response_json = response.json()
        assert "track" in response_json