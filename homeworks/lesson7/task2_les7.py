"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
 заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
  и отсортированный массивы.
"""
import random

size_down = 0
size_up = 50
array = [i for i in range(size_down, size_up)]
random.shuffle(array)
print(array)


def merge_sort(array):
    if len(array) < 2:
        return array[:]
    else:
        middle = int(len(array) / 2)
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

sort_array = merge_sort(array)
print(sort_array)
