# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий
# набор натуральных чисел. У пользователя необходимо запрашивать новый элемент
# рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то
# новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде,
# например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
vrem_list = []

while True:
    try:
        natural_var = input('Введите натруальное число отражающее новый элемент рейтинга: ')
        if natural_var.isdigit():
            int_natural_var = int(natural_var)
            if int_natural_var >= 0:
                break
    except ValueError:
        continue

if my_list.count(int_natural_var) == 0:
    for ind, element in enumerate(my_list):
        if element > int_natural_var:
            if len(my_list) - 1 == ind:
                my_list.insert(ind + 1, int_natural_var)
                print(my_list)
                break
        elif element < int_natural_var:
            my_list.insert(ind, int_natural_var)
            print(my_list)
            break
elif my_list.count(int_natural_var) == 1:
    index_element = my_list.index(int_natural_var)
    my_list.insert(index_element + 1, int_natural_var)
elif my_list.count(int_natural_var) > 1:
    vrem_list = my_list[:]
    vrem_list.reverse()
    index_element = vrem_list.index(int_natural_var)
    len_var_list = len(my_list)
    my_list.insert(len_var_list - index_element, int_natural_var)
    print(my_list)
