import pytest
import requests
from urls import CREATE_ORDER
from helpers import get_order_payload
import allure

@allure.epic("Создание заказа")
@allure.feature("API /api/v1/orders")
class TestCreateOrders:

    @allure.title("Создание заказа с цветом: {color}")
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order_with_colors(self, color):
        payload = get_order_payload(color)
        response = requests.post(CREATE_ORDER, json=payload)
        assert response.status_code == 201

    @allure.title("Проверка наличия track в ответе")
    def test_create_order_returns_track(self):
        payload = get_order_payload()
        response = requests.post(CREATE_ORDER, json=payload)
        assert response.status_code == 201

        response_json = response.json()
        assert "track" in response_json