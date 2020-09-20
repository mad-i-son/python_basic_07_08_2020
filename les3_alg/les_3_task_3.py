"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

var_list = [random.randint(0, 100) for _ in range(10)]
var_temp_max = var_list[0]
ind_temp_max = 0
var_temp_min = var_list[0]
ind_temp_min = 0
for ind, value in enumerate(var_list):
    if value > var_temp_max:
        var_temp_max = value
        ind_temp_max = ind
    if value < var_temp_min:
        var_temp_min = value
        ind_temp_min = ind

print(f'Начальный массив: {var_list}')
var_list[ind_temp_max] = var_temp_min
var_list[ind_temp_min] = var_temp_max
print(f'Измененный массив: {var_list}')
print(f'Минимальное число: {var_temp_min}')
print(f'Максимальное число: {var_temp_max}')
