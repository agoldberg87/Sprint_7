import pytest
import allure
from user import User

class TestUser():

    @allure.title('Проверка заказа')
    @pytest.mark.parametrize("color",
                         ["BLACK",
                          "GREY",
                          "BLACK, GREY",
                          ""
                          ])
    def test_place_order(self, color):
        user = User()
        user.place_order(color)

        assert user.response.status_code == 201, "Ожидаемый код ответа 201"
        assert user.response.json()["track"] is not None, "В ответе должен быть трек-номер"

    @allure.title('Проверка выгрузки заказов')
    def test_get_orders(self):
        user = User()
        user.place_order(user.color)
        user.get_orders()

        assert user.response.status_code == 200, "Ожидаемый код ответа 200"
        assert user.response.json()["orders"] is not None, "В ответе должна быть информация о заказах"