"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр
и вывести на экран. Например, если введено число 3486, надо вывести 6843.
"""

user_var = input('Введите число: ')
symbols = list(user_var)
for el in range(len(user_var) // 2):
    tmp = symbols[el]
    symbols[el] = symbols[len(user_var) - el - 1]
    symbols[len(user_var) - el - 1] = tmp
str_reverse = ''.join(symbols)
print(str_reverse)
