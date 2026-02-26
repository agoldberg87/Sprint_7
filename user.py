import requests
import allure
from helpers import generate_random_string
from order import Order
from data import ENDPOINTS

class User():

    def __init__(self):
        self.login = generate_random_string(10)
        self.password = generate_random_string(10)
        self.first_name = generate_random_string(10)

    # метод регистрации нового курьера возвращает кортеж из (response, login_pass)
    # если регистрация не удалась, login_pass будет пустым списком
    @allure.step('Регистрация нового курьера')
    def register_new_courier_and_return_login_password(self, login = None, password = None, first_name = None):

        # создаём список, чтобы метод мог его вернуть
        login_pass = []

        # подтягиваем логин, пароль и имя курьера, если они не предоставлены
        if login == None:
            login = self.login
        if password == None:
            password = self.password
        if first_name == None:
            first_name = self.first_name

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(ENDPOINTS.CREATE_COURIER, data=payload)

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        return response, login_pass
    

    @allure.step('Логин курьера')
    def login_user(self, login, password):
        # собираем тело запроса
        payload = {
            "login": login,
            "password": password
        }

        # отправляем запрос на логин курьера и сохраняем ответ в переменную response
        response = requests.post(ENDPOINTS.LOGIN_COURIER, data=payload)

        return response
    

    @allure.step('Удалить курьера')
    def delete_courier(self, courier_id):

        # отправляем запрос на удаление курьера и сохраняем ответ в переменную response
        response = requests.delete(f'{ENDPOINTS.DELETE_COURIER}{courier_id}')

        return response