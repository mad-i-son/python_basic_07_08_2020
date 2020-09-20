"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны
 каждому из чисел в диапазоне от 2 до 9. Примечание: 8 разных ответов.
"""

for var in range(2, 10):
    number_resolved = 0
    for value in range(2, 100):
        devision = value % var
        if devision == 0:
            number_resolved += 1
    print(f'Числу {var} кратоно {number_resolved} чисел от 2 до 99')
