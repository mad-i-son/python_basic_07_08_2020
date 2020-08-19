"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить
 результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce

def my_func (prev_el, el):
    """
    :param prev_el: int - предыдущий элемент
    :param el: int - текущий элемент
    """
    return prev_el * el

user_var = [el for el in range(100, 1001) if el % 2 == 0]

print(reduce(my_func, user_var))

