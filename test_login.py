import allure
from user import User

class TestUser():
    
    @allure.title('Проверка логина пользователя')
    def test_login_user(self):
        user = User()
        login_pass = user.register_new_courier_and_return_login_password()
        user.login_user(login=login_pass[0], password=login_pass[1])
        
        assert user.response.status_code == 200
        assert user.response.json()["id"] != None, "ID пользователя не вернулось"

    @allure.title('Проверка логина пользователя с неверным логином')
    def test_login_user_with_wrong_password(self):
        user = User()
        login_pass = user.register_new_courier_and_return_login_password()
        user.login_user(login="not_existing_login", password=login_pass[1])
        
        assert user.response.status_code == 404, "Ожидаемый код ответа 404"
        assert user.response.json()["message"] == "Учетная запись не найдена", "Ожидается сообщение об ошибке"

    @allure.title('Проверка логина пользователя без логина')
    def test_login_user_with_no_login(self):
        user = User()
        login_pass = user.register_new_courier_and_return_login_password()
        user.login_user(login="", password=login_pass[1])
        
        assert user.response.status_code == 400, "Ожидаемый код ответа 400"
        assert user.response.json()["message"] == "Недостаточно данных для входа", "Ожидается сообщение об ошибке"
    