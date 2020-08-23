"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на
русские. Новый блок строк должен записываться в новый текстовый файл.
"""

from pathlib import Path

var_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
file_name = 'les5_task4.txt'
file_name_new = 'les5_task4_new.txt'
file_path = Path(__file__).parent.joinpath(file_name)
file_path_new = Path(__file__).parent.joinpath(file_name_new)
var_list = []
user_str = ""
with open(file_path, 'r', encoding='UTF-8') as file:
    content = file.readlines()
    for elem in content:
        var_list = elem[:-1].split(' ')
        user_str = var_dict.get(var_list[0]) + " " + var_list[1] + " " + var_list[2]
        try:
            with open(file_path_new, 'a', encoding='UTF-8') as file:
                file.write(user_str + '\n')
        except FileNotFoundError:
            with open(file_path_new, 'w', encoding='UTF-8') as file:
                file.write(user_str + '\n')
    print('Выполнено')
