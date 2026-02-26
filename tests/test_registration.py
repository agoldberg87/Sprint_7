import allure
import pytest
import data

class TestRegistrationUser():

    @allure.title('Проверка регистрации нового курьера')
    def test_create_user(self, unregistered_user, delete_courier): # Позитивный сценарий
        user = unregistered_user

        response, login_pass = user.register_new_courier_and_return_login_password()
        
        assert response.status_code == 201, "Регистрация неуспешна - ожидаемый код ответа 201"
        assert response.ok == True, "Регистрация неуспешна - ожидается ok True"
        assert login_pass[0] is not None, "Логин не должен быть None"
        assert login_pass[1] is not None, "Пароль не должен быть None"
        assert login_pass[2] is not None, "Имя не должно быть None"
        
        # Очистка после успешной регистрации
        # Фикстура unregistered_user и успешная регистрация есть только в этом тесте, поэтому не стал дополнять фикстуру очисткой, а добавил ее в тело теста
        login_response = user.login_user(login=login_pass[0], password=login_pass[1])
        if login_response.json().get("id"):
            delete_courier(login_response.json()["id"])


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

    @allure.title('Проверка удаления курьера')
    def test_delete_user(self, registered_user):
        user, response, login_pass = registered_user
        
        login_response = user.login_user(login=login_pass[0], password=login_pass[1])
        courier_id = login_response.json()["id"]
        
        response = user.delete_courier(courier_id)
        assert response.status_code == 200, "Удаление неуспешно - ожидаемый код ответа 200"
        assert response.json()["ok"] == True, "Удаление неуспешно - ожидается ok True"