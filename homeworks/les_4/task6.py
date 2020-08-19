"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении
 числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие, при котором
  повторение элементов списка будет прекращено.
"""
# Скрипт запускать со строкой python homeworks\les_4\task6.py 3 ABCD



from itertools import count
from itertools import cycle
from sys import argv

def user_iteration(user_var):
    for el in count(user_var):
        if el == 10:
            break
        else :
            print(el)

def user_cycle_interation(user_list):
    с = 0
    for el in cycle(user_list):
        if с == 10:
            break
        print(el)
        с += 1

_, user_var, user_list = argv

user_iteration(int(user_var))
user_cycle_interation(user_list)

