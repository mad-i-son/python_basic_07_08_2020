import os
from pathlib import Path
import json
import requests

file_name = 'les5.txt'
file_path = os.path.join(os.path.dirname(__file__), file_name)
file_path2 = Path(__file__).parent.joinpath(file_name)


response = requests.get('https://geekbrains.ru/')

with open(file_path2.parent.joinpath('gp.htm'), 'w', encoding='UTF-8') as file:
    file.write(response.text)

# os.path.isdir()

# print(file_path2.is_file())
#
# file = open(file_path2, 'r', encoding='UTF-8')

# for line in file:
#     print(line, end='')
#
# tmp = file.readlines()
# print(tmp)

# try:
#     tmp = file.read()
# except IOError as e:
#     print(e)
# finally:
#     file.close()

# print(tmp)

# with open(file_path2, 'r', encoding='UTF-8') as file:
#     file.seek(8)
#     print(file.read(2))
#     print(file.read(2))
#     print(file.tell())
#     file.seek(4)

# file_str = '\n##--New2 words2 to2 file2--##'
# with open(file_path2, 'r+', encoding='UTF-8') as file:
#     file.seek(15)
#     print(file.tell())
#     file.write(file_str)

# some_list = ['some string', 1, 2, 3, [1, 2, 3], True, False, None, {'key': 1, 'ke2': 2}, (1, 2)]
# j_data = json.dumps(some_list)
#
# with open(file_path2.parent.joinpath('data.json'), 'w', encoding='UTF-8') as file:
#     # file.write(j_data)
#     json.dump(some_list, file, ensure_ascii=False)

# with open(file_path2.parent.joinpath('data.json'), 'r', encoding='UTF-8') as file:
#     read_data = json.loads(file.read())
#
# print(type(read_data))
# print(read_data)
# print(j_data)
