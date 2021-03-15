from os import write
from faker import Faker
import csv
import random
fake = Faker('ru_RU')


def get_fake_row():
    return [
        fake.name(), fake.city_name(), fake.street_address(),fake.company(),
        fake.job(), fake.phone_number(), fake.free_email(),
        fake.date_of_birth(minimum_age=18, maximum_age=70),
        random.randint(20000,200000)
    ]

def generate_data(num_rows=10000):
    with open('salary.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f,delimiter = ';')
        for _ in range(num_rows):
            writer.writerow(get_fake_row())

if __name__ == '__main__':
    generate_data()