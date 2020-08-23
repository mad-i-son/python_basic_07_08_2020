"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
 выполнить подсчет количества строк, количества слов в каждой строке.
"""
from pathlib import Path

file_name = 'les5_task2.txt'
file_path = Path(__file__).parent.joinpath(file_name)

with open(file_path, 'r', encoding='UTF-8') as file:
    content = file.readlines()
    quantity_lines = len(content)
    print(f'Всего строк в файле: {quantity_lines}')
    for ind, elem in enumerate(content, 1):
        quantity_word = len(elem.split(' '))
        print(f'В строке {ind}, число слов: {quantity_word}')