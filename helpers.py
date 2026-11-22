import requests
import random
import string
from urls import CREATE_COURIER

def register_new_courier_and_return_login_password():
   
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
 
    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass

def create_random_courier():
    login = "".join(random.choices(string.ascii_lowercase, k=10))
    password = "".join(random.choices(string.ascii_lowercase, k=10))
    first_name = "".join(random.choices(string.ascii_lowercase, k=10))
    
    payload = {"login": login, "password": password, "firstName": first_name}
    response = requests.post(CREATE_COURIER, data = payload)
    
    return response, payload

def get_order_payload(color=None):
    if color is None:
        color = []

        return {
    "firstName": "Ксения",
    "lastName": "Яковлева",
    "address": "Москва, Шипиловская, д.34",
    "metroStation": 4,
    "phone": "+7 969 123 35 35",
    "rentTime": 5,
    "deliveryDate": "2026-11-26",
    "comment": "Позвонить за час",
    "color": color
}