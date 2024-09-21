import csv
from faker import Faker
import random

fake = Faker(locale='uk_UA')

# Dictionaries for father names
male_middle_names = ['Іванович', 'Петрович', 'Олексійович', 'Андрійович', 'Миколайович', 'Сергійович', 'Володимирович']
female_middle_names = ['Іванівна', 'Петрівна', 'Олексіївна', 'Андріївна', 'Миколаївна', 'Сергіївна', 'Володимирівна']

def generate_employee(gender):
    if gender == 'Чоловік':
        first_name = fake.first_name_male()
        middle_name = random.choice(male_middle_names)
    else:
        first_name = fake.first_name_female()
        middle_name = random.choice(female_middle_names)
    
    return [
        fake.last_name(), first_name, middle_name, gender,
        fake.date_of_birth(minimum_age=16, maximum_age=85),
        fake.job(), fake.city_name(), fake.address(),
        fake.phone_number(), fake.email()
    ]

# Write data to CSV
with open('employees.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Прізвище', 'Ім’я', 'По батькові', 'Стать', 'Дата народження', 'Посада', 'Місто проживання', 'Адреса проживання', 'Телефон', 'Email'])

    for _ in range(1200):
        writer.writerow(generate_employee('Чоловік'))
    for _ in range(800):
        writer.writerow(generate_employee('Жінка'))
