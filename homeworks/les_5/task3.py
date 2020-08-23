"""
3. Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад
менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней
величины дохода сотрудников.
"""

from pathlib import Path

file_name = 'les5_task3.txt'
file_path = Path(__file__).parent.joinpath(file_name)
var_list = []
avg_income = 0.0
static_income = 20000.0
with open(file_path, 'r', encoding='UTF-8') as file:
    content = file.readlines()
    for elem in content:
        var_list = elem[:-1].split(' ')
        if float(var_list[1]) < static_income:
            print(f'Есть сотрудник по фамилии: {var_list[0]}, его оклад меньше 20000')
        avg_income += float(var_list[1])
    avg_income = avg_income / 3
    print(f'Средняя величина дохода сотрудников: {avg_income}')
