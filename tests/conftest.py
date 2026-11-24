import pytest
from helpers import create_random_courier
from api_client import login_courier, delete_courier

@pytest.fixture
def courier_data():
    _, payload = create_random_courier()
    
    login_response = login_courier({"login": payload["login"], "password": payload["password"]})
    courier_id = login_response.json()["id"]
    
    yield payload
    
    delete_courier(courier_id)