import allure
from user import User

class TestUser():

    @allure.title('Проверка регистрации нового курьера')
    def test_create_user(self): # Позитивный сценарий
        user = User()
        login_pass = user.register_new_courier_and_return_login_password()
        
        assert user.response.status_code == 201, "Регистрация неуспешна - ожидаемый код ответа 201"
        assert user.response.ok == True, "Регистрация неуспешна - ожидается ok True"
        assert login_pass[0] is not None, "Логин не должен быть None"
        assert login_pass[1] is not None, "Пароль не должен быть None"
        assert login_pass[2] is not None, "Имя не должно быть None"


    @allure.title('Проверка регистрации нового курьера без части данных (логина)')
    def test_create_user_with_empty_login(self): # Регистрация без части данных (логина)
        user = User()
        user.register_new_courier_and_return_login_password(login="")

        assert user.response.status_code == 400, "Регистрация НЕ МОЖЕТ быть успешной - ожидаемый код ответа 400"
        assert user.response.json()["message"] == "Недостаточно данных для создания учетной записи", "Регистрация НЕ МОЖЕТ быть успешной - ожидается сообщение об ошибке"

    
    @allure.title('Проверка регистрации нового курьера с уже существующими данными (логином)')
    def test_create_duplicate_user(self): # Повторная регистрация с уже существующими данными (логином)
        user = User()
        login_pass = user.register_new_courier_and_return_login_password()
        user.register_new_courier_and_return_login_password(login=login_pass[0])

        assert user.response.status_code == 409, "Регистрация НЕ МОЖЕТ быть успешной - ожидаемый код ответа 409"
        assert user.response.json()["message"] == "Этот логин уже используется. Попробуйте другой.", "Регистрация НЕ МОЖЕТ быть успешной - ожидается сообщение об ошибке"