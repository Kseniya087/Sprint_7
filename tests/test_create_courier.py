import requests
from helpers import register_new_courier_and_return_login_password
from urls import CREATE_COURIER
from helpers import create_random_courier
import allure

@allure.epic("Создание курьера")
@allure.feature("API /api/v1/courier")
class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self):
        courier_data = register_new_courier_and_return_login_password()
        assert len(courier_data) > 0

    @allure.title("Ошибка при создании дубликата")
    def test_create_dublicate_courier_error(self):
        courier_data = register_new_courier_and_return_login_password()
        login = courier_data[0]
        password = courier_data[1]
        first_name = courier_data[2]
        payload = {"login": login, "password": password, "firstName": first_name}
        response = requests.post(CREATE_COURIER, data = payload)
        assert response.status_code == 409

    @allure.title("Создание курьера с передачей всех обязательных полей")
    def test_create_courier_with_all_fields(self):
        response, _ = create_random_courier()
        assert response.status_code == 201

    @allure.title("Запрос возвращает правильный код ответа")
    def test_create_courier_retuns_correct_status_code(self):
        response, _= create_random_courier()
        assert response.status_code == 201

    @allure.title("Успешное создание курьера возвращает статус ok")
    def test_create_courier_retuns_ok_true(self):
        response, _ = create_random_courier()
        assert response.json() == {"ok": True}

    @allure.title("ОШибка, если не передано одно из обязательных полей")
    def test_create_courier_missing_field_error(self):
        fake_login = "some_login"
        fake_name = "TestName"
        payload = {"login": fake_login, "firstName": fake_name}
        response = requests.post(CREATE_COURIER, data = payload)
        assert response.status_code == 400

    @allure.title("ОШибка при создании курьера с сущетсвующим логином")
    def test_create_courier_existing_login_error(self):
        response_first, payload_first = create_random_courier()
        existing_login = payload_first["login"]
        payload_second = {"login": existing_login, "password": "Gfhjkm123", "firstName": "Second"}
        response_second = requests.post(CREATE_COURIER, data = payload_second)
        assert response_second.status_code == 409

