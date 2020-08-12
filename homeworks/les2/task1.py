# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать
# функцию type() для проверки типа. Элементы списка можно не запрашивать
# у пользователя, а указать явно, в программе.

var_list = []

var_list.append(True)
var_list.append(2)
var_list.append(2.5)
var_list.append('Max')
var_list.append([1, 2, 3])
var_list.append((1, 2, 3))
var_list.append({1, 2, 3})
var_list.append({'day': 11, 'month': 3})

for var_elements in var_list:
    if type(var_elements) is bool:
        print(f'Это буллево значение - {var_elements}')
    elif type(var_elements) is int:
        print(f'Это целое число - {var_elements}')
    elif type(var_elements) is float:
        print(f'Это число с плавающей запятой - {var_elements}')
    elif type(var_elements) is str:
        print(f'Это строка - {var_elements}')
    elif type(var_elements) is list:
        print(f'Это список - {var_elements}')
    elif type(var_elements) is tuple:
        print(f'Это кортеж - {var_elements}')
    elif type(var_elements) is set:
        print(f'Это множество - {var_elements}')
    else:
        print(f'Это словарь - {var_elements}')
