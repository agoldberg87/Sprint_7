class ENDPOINTS:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"
    
    CREATE_COURIER = f"{BASE_URL}/courier"
    LOGIN_COURIER = f"{BASE_URL}/courier/login"
    DELETE_COURIER = f"{BASE_URL}/courier/"
    
    CREATE_ORDER = f"{BASE_URL}/orders"
    GET_ORDERS = f"{BASE_URL}/orders"

# ответы бэкэнда
insufficient_registration_data_message = "Недостаточно данных для создания учетной записи"
occupied_login_message = "Этот логин уже используется. Попробуйте другой."
login_not_found_message = "Учетная запись не найдена"
insufficient_login_data_message = "Недостаточно данных для входа"
