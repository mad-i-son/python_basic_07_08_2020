# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

while True:
    try:
        user_word = input('Введите строку из нескольких слов, разделённых пробелами: ')
        break
    except ValueError:
        continue

var_list = user_word.split()

for ind, element in enumerate(var_list, 1):
    print(ind, element[:10])
