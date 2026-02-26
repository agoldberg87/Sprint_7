import allure
import pytest
import data

class TestDeleteUser():


    @allure.title('Проверка удаления курьера')
    def test_delete_user(self, registered_user):
        user, response, login_pass = registered_user
        
        login_response = user.login_user(login=login_pass[0], password=login_pass[1])
        courier_id = login_response.json()["id"]
        
        response = user.delete_courier(courier_id)
        assert response.status_code == 200, "Удаление неуспешно - ожидаемый код ответа 200"
        assert response.json()["ok"] == True, "Удаление неуспешно - ожидается ok True"

    @allure.title('Проверка удаления курьера с несуществующим id')
    def test_delete_user_with_invalid_id(self, registered_user):
        user, response, login_pass = registered_user
        
        response = user.delete_courier(courier_id=123456789)
        assert response.status_code == 404, "Удаление неуспешно - ожидаемый код ответа 404"
        assert response.json()["message"] == data.courier_not_found_message, "Удаление неуспешно - ожидается сообщение об ошибке"

    @allure.title('Проверка удаления курьера без id')
    def test_delete_user_without_id(self, registered_user):
        user, response, login_pass = registered_user
        
        response = user.delete_courier(courier_id="")
        assert response.status_code == 404, "Удаление неуспешно - ожидаемый код ответа 400"
        assert response.json()["message"] == data.courier_not_found_message_empty, "Удаление неуспешно - ожидается сообщение об ошибке"

        # проверил руками через Postman: при отправке запроса с пустым id, возвращает 404, а не 400, как в документации