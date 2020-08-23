"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка
описывает учебный предмет и наличие лекционных, практических и лабораторных
занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
не обязательно были все типы занятий. Сформировать словарь, содержащий
название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

from pathlib import Path

file_name = 'les5_task6.txt'
file_path = Path(__file__).parent.joinpath(file_name)
new_dict = {}
var_list = []

with open(file_path, 'r', encoding='UTF-8') as file:
    content = file.readlines()
    for elem in content:
        var_sum = 0.0
        var_list = elem[:-1].split(' ')
        for ind, elem_list in enumerate(var_list):
            if ind == 0:
                new_dict.setdefault(elem_list)
            else:
                if elem_list.count('(л)') > 0:
                    var_sum += float(elem_list.replace('(л)', ''))
                elif elem_list.count('(пр)') > 0:
                    var_sum += float(elem_list.replace('(пр)', ''))
                elif elem_list.count('(лаб)') > 0:
                    var_sum += float(elem_list.replace('(лаб)', ''))
        new_dict[var_list[0]] = var_sum
    print(new_dict)
