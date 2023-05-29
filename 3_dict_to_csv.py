"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    workers = [
        {'name': 'Иван', 'age': 18, 'job': 'Программист'},
        {'name': 'Илья', 'age': 27, 'job': 'Дворник'},
        {'name': 'Игорь', 'age': 52, 'job': 'Врач'},
        {'name': 'Дантес', 'age': 26, 'job': 'Инженер'},
        {'name': 'Сантос', 'age': 27, 'job': 'Комик'},
        {'name': 'Сальвадор', 'age': 28, 'job': 'Фронтендер'},
        {'name': 'Настя', 'age': 27, 'job': 'Лектор'}
    ]
    with open('workers.csv', 'w', encoding='utf-8') as f:
        headers = workers[0].keys()
        writer = csv.DictWriter(f, headers, delimiter=';')
        writer.writeheader()
        for worker in workers:
            writer.writerow(worker)

if __name__ == "__main__":
    main()
