import requests
import allure
from urls import BASE_URL

@allure.step("Создать курьера")
def create_courier(payload):
    return requests.post(f"{BASE_URL}/api/v1/courier", data=payload)

@allure.step("Логин курьера")
def login_courier(payload):
    return requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload)

@allure.step("Удалить курьера по ID: {courier_id}")
def delete_courier(courier_id):
    return requests.delete(f"{BASE_URL}/api/v1/courier/{courier_id}")

@allure.step("Создать заказ")
def create_order(payload):
    return requests.post(f"{BASE_URL}/api/v1/orders", json=payload)

@allure.step("Получить список заказов")
def get_orders_list():
    return requests.get(f"{BASE_URL}/api/v1/orders")