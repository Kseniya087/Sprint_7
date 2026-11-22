import pytest
import requests
from helpers import create_random_courier, delete_courier
from urls import LOGIN_COURIER

@pytest.fixture
def courier_data():
    _, payload = create_random_courier()
    
    login_response = requests.post(
        LOGIN_COURIER, 
        data={"login": payload["login"], "password": payload["password"]}
    )
    courier_id = login_response.json()["id"]
    
    yield payload
    
    delete_courier(courier_id)