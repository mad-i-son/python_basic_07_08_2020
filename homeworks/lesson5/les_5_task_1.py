"""
1. Пользователь вводит данные о количестве предприятий, их наименования
прибыль за четыре квартала для каждого предприятия. Программа должна
определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import Counter

count_factory = int(input('Введите количество предприятий: '))
user_dict = Counter()
for i in range(count_factory):
    name_factory = input('Введите название предприятия: ')
    money_factory = float(input('Введите прибыль предприятия за квартал: '))

    user_dict[name_factory] = money_factory*3

sum = 0.0
count = 0.0
for value in user_dict.values():
    sum += value
    count += 1
medium_sum = sum / count

temp_dict = Counter()

for key in user_dict.keys():
    temp_dict[key] = medium_sum

new_dict = user_dict - temp_dict

for key in new_dict.keys():
    print(f'У предприятия {key} получилась прибыль выше средней на {new_dict.setdefault(key)} при средней прибыли {medium_sum}')

for key in user_dict.keys():
    if user_dict.setdefault(key) < medium_sum:
        print(f'У предприятия {key} получилась прибыль ниже средней а именно {user_dict.setdefault(key)} при средней прибыли {medium_sum}')
