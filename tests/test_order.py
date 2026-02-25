import pytest
import allure
from order import Order

class TestOrderUser():

    @allure.title('Проверка заказа')
    @pytest.mark.parametrize("color",
                         ["BLACK",
                          "GREY",
                          "BLACK, GREY",
                          ""
                          ])
    def test_place_order(self, color):
        order = Order()
        response = order.place_order(color)

        assert response.status_code == 201, "Ожидаемый код ответа 201"
        assert response.json()["track"] is not None, "В ответе должен быть трек-номер"

    @allure.title('Проверка выгрузки заказов')
    def test_get_orders(self):
        order = Order()
        order.place_order(order.color)
        response = order.get_orders()

        assert response.status_code == 200, "Ожидаемый код ответа 200"
        assert response.json()["orders"] is not None, "В ответе должна быть информация о заказах"