"""
2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если
 введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

user_var = int(input('Введите число: '))
qount_even_number = 0
qount_uneven_number = 0

while True:
    numeric = user_var % 10

    if numeric % 2 > 0:
        qount_uneven_number += 1
    else:
        qount_even_number += 1

    user_var //= 10
    if user_var == 0:
        break

print(f'Нечетных чисел: {qount_uneven_number}; четные чисел: {qount_even_number}')