import requests
import random
import allure
from helpers import generate_random_string, generate_random_phone
from data import ENDPOINTS

class Order():
    
    def __init__(self):
        self.first_name = generate_random_string(10)
        self.last_name = generate_random_string(10)
        self.address = generate_random_string(10)
        self.metro_station = "Сокол"
        self.phone = generate_random_phone()
        self.rent_time = random.randint(1, 10)
        self.delivery_date = "2023-03-10"
        self.comment = generate_random_string(10)
        self.color = ["BLACK", "GREY"]

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
        response = requests.post(ENDPOINTS.CREATE_ORDER, json=payload_order)

        # возвращаем response
        return response
    

    @allure.step('Получить список заказов')
    def get_orders(self):

        # отправляем запрос на получение списка заказов и сохраняем ответ в переменную response
        response = requests.get(ENDPOINTS.GET_ORDERS)

        # возвращаем response
        return response