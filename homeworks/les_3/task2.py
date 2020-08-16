"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод
данных о пользователе одной строкой.
"""


def description_user(name, surname, year, user_city, user_email, user_phone):
    if type(name) == str and type(surname) == str and type(year) == int and type(user_city) == str \
            and type(user_email) == str and type(user_phone) == str:
        return (f'Имя и Фамилия пользователя: {name} {surname}, год рождения: {year},'
                f''f'город проживания: {user_city}, email: {user_email}, телефон: {user_phone}')
    else:
        return ('Аргументы функции введены не правильно, попробуйте ещё раз.')
