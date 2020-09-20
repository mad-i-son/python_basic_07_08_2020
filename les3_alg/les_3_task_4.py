"""
4. Определить, какое число в массиве встречается чаще всего.
"""
import random

var_list = [random.randint(0, 10) for _ in range(5)]

max_num = var_list[0]
qount_max_num = 0

for ind, value in enumerate(var_list):
    qouunt_ind = 0
    for ind_two, value_two in enumerate(var_list):
        if value == value_two:
            qouunt_ind += 1
    if qount_max_num < qouunt_ind:
        qount_max_num = qouunt_ind
        max_num = value
print(f'Исходный массив: {var_list}')
print(f'Число в массиве встречающееся чаще всего: {max_num}')
