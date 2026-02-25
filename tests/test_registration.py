import allure
import pytest
import data

class TestRegistrationUser():

    @allure.title('Проверка регистрации нового курьера')
    def test_create_user(self, registered_user): # Позитивный сценарий
        user, response, login_pass = registered_user
        
        assert response.status_code == 201, "Регистрация неуспешна - ожидаемый код ответа 201"
        assert response.ok == True, "Регистрация неуспешна - ожидается ok True"
        assert login_pass[0] is not None, "Логин не должен быть None"
        assert login_pass[1] is not None, "Пароль не должен быть None"
        assert login_pass[2] is not None, "Имя не должно быть None"


    @allure.title('Проверка регистрации нового курьера без части данных (логина)')
    def test_create_user_with_empty_login(self, unregistered_user): # Регистрация без части данных (логина)
        user = unregistered_user
        response, login_pass = user.register_new_courier_and_return_login_password(login="")

        assert response.status_code == 400, "Регистрация НЕ МОЖЕТ быть успешной - ожидаемый код ответа 400"
        assert response.json()["message"] == data.insufficient_registration_data_message, "Регистрация НЕ МОЖЕТ быть успешной - ожидается сообщение об ошибке"

    
    @allure.title('Проверка регистрации нового курьера с уже существующими данными (логином)')
    def test_create_duplicate_user(self, registered_user): # Повторная регистрация с уже существующими данными (логином)
        user, response, login_pass = registered_user
        response, login_pass = user.register_new_courier_and_return_login_password(login=login_pass[0])

        assert response.status_code == 409, "Регистрация НЕ МОЖЕТ быть успешной - ожидаемый код ответа 409"
        assert response.json()["message"] == data.occupied_login_message, "Регистрация НЕ МОЖЕТ быть успешной - ожидается сообщение об ошибке"