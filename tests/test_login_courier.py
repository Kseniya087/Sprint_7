import requests
import pytest
from urls import LOGIN_COURIER
from helpers import create_random_courier
import allure

@allure.epic("Логин курьера")
@allure.feature("API /api/v1/courier/login")
class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_login_courier_success(self):
        _,payload = create_random_courier()
        login_data = {"login": payload["login"],
        "password": payload["password"]}
        response = requests.post(LOGIN_COURIER, data = login_data)
        assert response.status_code == 200

    @allure.title("Успешная авторизация с передачей всех обязательных полей")
    def test_login_courier_with_all_fields(self):
        _,payload = create_random_courier()
        login_data = {"login": payload["login"],
                "password": payload["password"]}
        response = requests.post(LOGIN_COURIER, data = login_data)
        assert response.status_code == 200

    @allure.title("Возврат ошибки при неверном логине или пароле")
    def test_login_courier_wrong_credentials_error(self):
        _,payload = create_random_courier()
        login_data = {"login": payload["login"],
                "password": "wrong_password_123"}
        response = requests.post(LOGIN_COURIER, data = login_data)
        assert response.status_code == 404

    @allure.title("Возврат ошибки при отсутствии обязательного поля")
    @pytest.mark.parametrize("login_data", [{"login": "some_test_login"},
                   {"password": "some_test_password"},{}])
    def test_login_courier_missing_field_error(self, login_data):
        response = requests.post(LOGIN_COURIER, data = login_data)
        assert response.status_code in [400, 504]

    @allure.title("Запрос возвращает ошибку при авторизации под несуществующим пользователем")
    def test_login_courier_non_existent_user_error(self):
        login_data = {"login":"login_6060",
                    "password":"password_6060"}
        response = requests.post(LOGIN_COURIER, data = login_data)
        assert response.status_code == 404
    
    @allure.title("успешный запрос возвращает 'id' курьера в теле ответа")
    def test_login_courier_retuns_id(self):
        _,payload = create_random_courier()
        login_data = {"login": payload["login"],
             "password": payload["password"]}
        response = requests.post(LOGIN_COURIER, data = login_data)
        assert "id" in response.json()