import requests
import random
import string
import allure

class User():

    @staticmethod
    def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

    def __init__(self):
        self.login = self.generate_random_string(10)
        self.password = self.generate_random_string(10)
        self.first_name = self.generate_random_string(10)
        self.last_name = self.generate_random_string(10)
        self.address = self.generate_random_string(10)
        self.metro_station = "Сокол"
        self.phone = f"+7{random.randint(9000000000, 9999999999)}"
        self.rent_time = random.randint(1, 10)
        self.delivery_date = "2023-03-10"
        self.comment = self.generate_random_string(10)
        self.color = ["BLACK", "GREY"]
        self.response = None

    # метод регистрации нового курьера возвращает список из логина и пароля
    # если регистрация не удалась, возвращает пустой список
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
        self.response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if self.response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        # возвращаем список
        return login_pass
    

    @allure.step('Логин курьера')
    def login_user(self, login, password):
        # собираем тело запроса
        payload = {
            "login": login,
            "password": password
        }

        # отправляем запрос на логин курьера и сохраняем ответ в переменную response
        self.response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)

        # возвращаем ответ
        return self.response.json()
    
    @allure.step('Создать заказ')
    def place_order(self, color):

        # собираем тело запроса
        payload_order = {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "address": self.address,
            "metroStation": self.metro_station,
            "phone": self.phone,
            "rentTime": self.rent_time,
            "deliveryDate": self.delivery_date,
            "comment": self.comment,
            "color": [color] if color else []
        }
                
        # отправляем запрос на создание заказа и сохраняем ответ в переменную response
        self.response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=payload_order)

        # возвращаем ответ
        return self.response.json()
    

    @allure.step('Получить список заказов')
    def get_orders(self):

        # отправляем запрос на получение списка заказов и сохраняем ответ в переменную response
        self.response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')

        # возвращаем ответ
        return self.response.json()