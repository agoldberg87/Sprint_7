import allure
import pytest
import data

class TestLoginUser():
    
    @allure.title('Проверка логина пользователя')
    def test_login_user(self, registered_user):
        user, response, login_pass = registered_user
        response = user.login_user(login=login_pass[0], password=login_pass[1])
        
        assert response.status_code == 200
        assert response.json()["id"] != None, "ID пользователя не вернулось"

    @allure.title('Проверка логина пользователя с неверным логином')
    def test_login_user_with_wrong_password(self, registered_user):
        user, response, login_pass = registered_user
        response = user.login_user(login="not_existing_login", password=login_pass[1])
        
        assert response.status_code == 404, "Ожидаемый код ответа 404"
        assert response.json()["message"] == data.login_not_found_message, "Ожидается сообщение об ошибке"

    @allure.title('Проверка логина пользователя без логина')
    def test_login_user_with_no_login(self, registered_user):
        user, response, login_pass = registered_user
        response = user.login_user(login="", password=login_pass[1])
        
        assert response.status_code == 400, "Ожидаемый код ответа 400"
        assert response.json()["message"] == data.insufficient_login_data_message, "Ожидается сообщение об ошибке"
    