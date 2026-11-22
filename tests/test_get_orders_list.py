import requests
from urls import GET_ORDERS_LIST
import allure

@allure.epic("Список заказов")
@allure.feature("API /api/v1/orders")
class TestOrdersList:

    @allure.title("Получение списка заказов")
    def test_get_orders_list_returns_orders(self):
        response = requests.get(GET_ORDERS_LIST)
        assert response.status_code == 200

        response_json = response.json()
        assert "orders" in response_json

