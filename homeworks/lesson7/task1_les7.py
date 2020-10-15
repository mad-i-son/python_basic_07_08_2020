"""
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
 заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход
массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться
сортировка пузырьком. Улучшенные версии сортировки, например, расчёской,
 шейкерная и другие в зачёт не идут.
"""
import random

size_down = - 100
size_up = 100
array = [i for i in range(size_down, size_up)]
random.shuffle(array)
print(array)

def bottle_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] == 0 and i != len(array)//2:
                array[len(array)//2], array[i] = array[i], array[len(array)//2]
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

        n += 1
    print(array)

bottle_sort(array)

