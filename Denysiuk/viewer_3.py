import csv
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

def read_csv(file_name):
    try:
        with open(file_name, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            return list(reader)
    except FileNotFoundError:
        print("CSV file not found.")
        return []

def plot_pie_chart(data, title, labels):
    plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title(title)
    plt.show()

def process_data():
    data = read_csv('employees.csv')
    if not data:
        return

    genders = [row[3] for row in data]
    gender_count = Counter(genders)
    print(f"Чоловіки: {gender_count['Чоловік']}, Жінки: {gender_count['Жінка']}")
    plot_pie_chart([gender_count['Чоловік'], gender_count['Жінка']], 'Статистика статі', ['Чоловіки', 'Жінки'])

    age_categories = {'younger_18': 0, '18-45': 0, '45-70': 0, 'older_70': 0}
    for row in data:
        birthdate = datetime.strptime(row[4], '%Y-%m-%d')
        age = calculate_age(birthdate)
        if age < 18:
            age_categories['younger_18'] += 1
        elif 18 <= age <= 45:
            age_categories['18-45'] += 1
        elif 45 < age <= 70:
            age_categories['45-70'] += 1
        else:
            age_categories['older_70'] += 1

    print("Кількість співробітників за віковими категоріями:", age_categories)
    plot_pie_chart(age_categories.values(), 'Вікові категорії', age_categories.keys())

process_data()
