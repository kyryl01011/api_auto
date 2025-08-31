from faker import Faker


class DataGenerator:
    def __init__(self, fake: Faker):
        self.fake = fake

    def generate_email(self):
        return self.fake.email()

    def generate_random_line(self, length: int = 10, special_chars: bool = False):
        return self.fake.password(length=length, special_chars=special_chars)

    def generate_name(self):
        return self.fake.first_name()

    def uuid(self):
        return self.fake.uuid4()


data_generator = DataGenerator(Faker())
