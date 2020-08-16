"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.
"""

def devided_var(var_1, var_2):
    print(var_1 / var_2)

while True:
    try:
        user_var1 = input('Введите первое целое число: ')
        user_var2 = input('Введите второе целое число: ')
        if user_var1.replace(".", "", 1).isdigit() and user_var2.replace(".", "", 1).isdigit():
            if float(user_var1) == 0 or float(user_var2) == 0:
                print('Деление на ноль запрещено попробуйте ввести цифры ещё раз.')

            else:
                devided_var(float(user_var1), float(user_var2))
                break
    except ValueError:
        continue


