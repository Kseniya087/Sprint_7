import pytest
from data import TestData
from api_client import create_courier
import allure

@allure.epic("Создание курьера")
@allure.feature("API /api/v1/courier")
class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self, created_courier):
        response, _ = created_courier
        assert response.status_code == 201
        assert response.json() == {"ok": True}


    @allure.title("Ошибка при создании дубликата")
    def test_create_dublicate_courier_error(self, created_courier):
        _, payload_first = created_courier
        dublicate_payload ={"login": payload_first["login"],
            "password": payload_first["password"], 
            "first_name": payload_first["firstName"]}

        response = create_courier(dublicate_payload)
        assert response.status_code == 409
        assert "message" in response.json()


    @allure.title("Создание курьера с передачей всех обязательных полей")
    def test_create_courier_with_all_fields(self, created_courier):
        response, _ = created_courier
        assert response.status_code == 201
        assert response.json() == {"ok": True}


    @allure.title("Запрос возвращает правильный код ответа")
    def test_create_courier_retuns_correct_status_code(self, created_courier):
        response, _ = created_courier
        assert response.status_code == 201


    @allure.title("Успешное создание курьера возвращает статус ok")
    def test_create_courier_retuns_ok_true(self, created_courier):
        response, _ = created_courier
        assert response.json() == {"ok": True}


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

