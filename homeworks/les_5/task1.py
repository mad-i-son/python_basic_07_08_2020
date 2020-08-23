"""
1. Создать программно файл в текстовом формате, записать в него построчно
 данные, вводимые пользователем. Об окончании ввода данных свидетельствует
  пустая строка.
"""
from pathlib import Path

file_name = 'les5_task1.txt'
file_path = Path(__file__).parent.joinpath(file_name)

while True:
    user_data = input('Введите данные которые надо записать в файл: ')
    if user_data == "":
        break
    else:
        try:
            with open(file_path, 'a', encoding='UTF-8') as file:
                file.write(user_data + '\n')
        except FileNotFoundError:
            with open(file_path, 'w', encoding='UTF-8') as file:
                file.write(user_data + '\n')
