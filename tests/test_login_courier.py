import pytest
from api_client import login_courier
import allure
from data import TestData

@allure.epic("Логин курьера")
@allure.feature("API /api/v1/courier/login")
class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_login_courier_success(self, courier_data):
        login_data = {"login": courier_data["login"],
        "password": courier_data["password"]}
        response = login_courier(login_data)
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Успешная авторизация с передачей всех обязательных полей")
    def test_login_courier_with_all_fields(self, courier_data):
        login_data = {"login": courier_data["login"],
                "password": courier_data["password"]}
        response = login_courier(login_data)
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Возврат ошибки при неверном логине или пароле")
    def test_login_courier_wrong_credentials_error(self, courier_data):
        login_data = {
            "login": courier_data["login"],
            "password": TestData.WRONG_PASSWORD
            }
        response = login_courier(login_data)
        assert response.status_code == 404
        assert "message" in response.json()

    @allure.title("Возврат ошибки при отсутствии обязательного поля")
    @pytest.mark.parametrize("login_data", [{"login": TestData.SOME_LOGIN},
                   {"password": TestData.SOME_PASSWORD},{}])
    def test_login_courier_missing_field_error(self, login_data):
        response = login_courier(login_data)
        assert response.status_code in [400, 504]
        if response.status_code == 400:
            assert "message" in response.json()

    @allure.title("Запрос возвращает ошибку при авторизации под несуществующим пользователем")
    def test_login_courier_non_existent_user_error(self):
        login_data = {"login": TestData.NON_EXISTENT_LOGIN,
                      "password": TestData.NON_EXISTENT_PASSWORD}
        response = login_courier(login_data)
        assert response.status_code == 404
        assert "message" in response.json()
    
    @allure.title("успешный запрос возвращает 'id' курьера в теле ответа")
    def test_login_courier_retuns_id(self, courier_data):
        login_data = {"login": courier_data["login"],
             "password": courier_data["password"]}
        response = login_courier(login_data)
        assert "id" in response.json()