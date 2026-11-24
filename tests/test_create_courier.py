import pytest
from data import TestData
from api_client import create_courier, login_courier, delete_courier
from helpers import create_random_courier, delete_courier_by_login
import allure

@allure.epic("Создание курьера")
@allure.feature("API /api/v1/courier")
class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self):
        response, payload = create_random_courier()
        assert response.status_code == 201
        assert response.json() == {"ok": True}

        delete_courier_by_login(payload["login"], payload["password"])

    @allure.title("Ошибка при создании дубликата")
    def test_create_dublicate_courier_error(self):
        _, payload_first = create_random_courier()
        dublicate_payload ={"login": payload_first["login"],
            "password": payload_first["password"], 
            "first_name": payload_first["firstName"]}

        response = create_courier(dublicate_payload)
        assert response.status_code == 409
        assert "message" in response.json()

        login_response = login_courier({"login": payload_first["login"],"password": payload_first["password"]})
        delete_courier(login_response.json()["id"])

    @allure.title("Создание курьера с передачей всех обязательных полей")
    def test_create_courier_with_all_fields(self):
        response, payload = create_random_courier()
        assert response.status_code == 201
        assert response.json() == {"ok": True}

        delete_courier_by_login(payload["login"], payload["password"])

    @allure.title("Запрос возвращает правильный код ответа")
    def test_create_courier_retuns_correct_status_code(self):
        response, payload = create_random_courier()
        assert response.status_code == 201

        delete_courier_by_login(payload["login"], payload["password"])

    @allure.title("Успешное создание курьера возвращает статус ok")
    def test_create_courier_retuns_ok_true(self):
        response, payload = create_random_courier()
        assert response.json() == {"ok": True}

        delete_courier_by_login(payload["login"], payload["password"])

    @allure.title("ОШибка, если не передано одно из обязательных полей")
    @pytest.mark.parametrize("payload", [
        {"login": TestData.FAKE_LOGIN, "firstName": TestData.FAKE_FIRST_NAME},
        {"password": TestData.FAKE_PASSWORD, "firstName": TestData.FAKE_FIRST_NAME}
        ])
    def test_create_courier_missing_field_error(self, payload):
        response = create_courier(payload)
        assert response.status_code == 400
        assert "message" in response.json()

    @allure.title("ОШибка при создании курьера с сущетсвующим логином")
    def test_create_courier_existing_login_error(self, courier_data):
        payload = {
            "login": courier_data["login"], 
            "password": TestData.FAKE_PASSWORD, "firstName": TestData.FAKE_FIRST_NAME}
        response = create_courier(payload)
        assert response.status_code == 409
        assert "message" in response.json()

