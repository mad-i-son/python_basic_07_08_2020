"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
  выводить ее на экран.
"""

from pathlib import Path

file_name = 'les5_task5.txt'
file_path = Path(__file__).parent.joinpath(file_name)
var_sum = 0
var_list = []
while True:
    user_data = input('Введите через пробел числа, которые надо записать в файл, для выхода введите просто пробел: ')
    if user_data == "":
        break
    else:
        var_list = user_data.split(" ")
        for elem in var_list:
            var_sum += float(elem)
        print(f'Сумму чисел в файле {var_sum}')
        try:
            with open(file_path, 'a', encoding='UTF-8') as file:
                file.write(user_data + '\n')
        except FileNotFoundError:
            with open(file_path, 'w', encoding='UTF-8') as file:
                file.write(user_data + '\n')