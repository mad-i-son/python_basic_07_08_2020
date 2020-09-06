"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
 Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
  нуля в качестве делителя программа должна корректно обработать эту ситуацию
   и не завершиться с ошибкой.
"""


class DevisionByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


user_var1 = input('Введите делимое: ')
user_var2 = input('Введите делитель: ')

try:
    user_var1 = float(user_var1)
    user_var2 = float(user_var2)
    if user_var2 < 0:
        raise DevisionByZero('Вы ввели отрицательное число')
    elif user_var2 == 0:
        raise DevisionByZero('Деление на ноль запрещено')
except ValueError:
    print("Вы ввели не число")
except DevisionByZero as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {user_var1 / user_var2} ")
