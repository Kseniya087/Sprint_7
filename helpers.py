import random
import string
from api_client import create_courier, login_courier, delete_courier

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def register_new_courier_and_return_login_password():
    login_pass = []
    
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = create_courier(payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass

def create_random_courier():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {"login": login, "password": password, "firstName": first_name}
    response = create_courier(payload)

    return response, payload

def get_order_payload(color):
    payload = {
        "firstName": "Ксения",
        "lastName": "Яковлева",
        "address": "ул.Шилова,д.34",
        "metroStation": 4,
        "phone": "+7 969 087 35 35",
        "rentTime": 5,
        "deliveryDate": "2026-11-26",
        "comment": "Позвонить за час",
        "color": color
    }
    return payload

def delete_courier_by_login(login, password):
    login_response = login_courier({"login": login, "password": password})
    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")
        if courier_id:
            delete_courier(courier_id)
                                            
