import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from user import User


@pytest.fixture
def registered_user(delete_courier):
    user = User()
    response, login_pass = user.register_new_courier_and_return_login_password()
    
    yield user, response, login_pass
    
    if response.status_code == 201:  # удаляем только при успешной регистрации
        # Получаем ID пользователя
        login_response = user.login_user(login=login_pass[0], password=login_pass[1])
        if login_response.json().get("id"):
            delete_courier(login_response.json()["id"])


@pytest.fixture
def unregistered_user():
    return User()

@pytest.fixture
def delete_courier():
    def _delete_courier(courier_id):
        user = User()
        return user.delete_courier(courier_id)
    return _delete_courier