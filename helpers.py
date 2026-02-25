import random
import string


def generate_random_string(length):
    """Generate a random string of lowercase letters with specified length."""
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_random_phone():
    """Generate a random Russian phone number starting with +7."""
    return f"+7{random.randint(9000000000, 9999999999)}"


def generate_user_data():
    """Generate random user data for testing purposes."""
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "first_name": generate_random_string(10),
        "last_name": generate_random_string(10),
        "address": generate_random_string(10),
        "phone": generate_random_phone(),
        "rent_time": random.randint(1, 10),
        "comment": generate_random_string(10)
    }