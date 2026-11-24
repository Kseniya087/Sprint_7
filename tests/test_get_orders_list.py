from api_client import get_orders_list
import allure

@allure.epic("Список заказов")
@allure.feature("API /api/v1/orders")
class TestOrdersList:

    @allure.title("Получение списка заказов")
    def test_get_orders_list_returns_orders(self):
        response = get_orders_list()
        assert response.status_code == 200

        response_json = response.json()
        assert "orders" in response_json

