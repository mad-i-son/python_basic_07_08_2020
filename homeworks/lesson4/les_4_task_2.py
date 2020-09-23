"""
2. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

# import random
# import cProfile
# def main():
#     var_list = [random.randint(0, 100) for _ in range(10)]
#     var_temp_max = var_list[0]
#     ind_temp_max = 0
#     var_temp_min = var_list[0]
#     ind_temp_min = 0
#     for ind, value in enumerate(var_list):
#         if value > var_temp_max:
#             var_temp_max = value
#             ind_temp_max = ind
#         if value < var_temp_min:
#             var_temp_min = value
#             ind_temp_min = ind
#
#     print(f'Начальный массив: {var_list}')
#     var_list[ind_temp_max] = var_temp_min
#     var_list[ind_temp_min] = var_temp_max
#     print(f'Измененный массив: {var_list}')
#     print(f'Минимальное число: {var_temp_min}')
#     print(f'Максимальное число: {var_temp_max}')
#
# cProfile.run('main()')

# 100 loops, best of 5: 31.7 nsec per loop

# 61 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:7(main)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:8(<listcomp>)
#        10    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:244(randint)
#        10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         4    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        12    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}



# from random import random
#
# n = 10
# arr = [0] * n
# mn = 0
# mx = 0
# for i in range(n):
#     arr[i] = int(random() * 100)
#     if arr[i] < arr[mn]:
#         mn = i
#     elif arr[i] > arr[mx]:
#         mx = i
# print(arr)
#
# b = arr[mn]
# arr[mn] = arr[mx]
# arr[mx] = b
#
# print(arr)

# 100 loops, best of 5: 27.2 nsec per loop



import random

array_size = 20
array = [random.randint(-100, 100) for _ in range(array_size)]
min_number = array[0]
max_number = array[0]
min_index = 0
max_index = 0

for ind in range(len(array)):
    if array[ind] < min_number:
        min_number = array[ind]
        min_index = ind
    elif array[ind] > max_number:
        max_number = array[ind]
        max_index = ind

print(array)
print(f'Меняем минимальное значение {min_number}, находящееся под индексом {min_index} с максимальным '
      f'значением {max_number}, находящемся под индексом {max_index}')
array[min_index], array[max_index] = array[max_index], array[min_index]
print(array)

# 100 loops, best of 5: 31.7 nsec per loop
