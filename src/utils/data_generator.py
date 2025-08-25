from faker import Faker

fake = Faker()


class DataGenerator:
    @staticmethod
    def generate_email():
        return fake.email(safe=True)

    @staticmethod
    def generate_random_line(length: int = 10, special_chars: bool = False):
        return fake.password(length=length, special_chars=special_chars)

    @staticmethod
    def generate_name():
        return fake.name()
