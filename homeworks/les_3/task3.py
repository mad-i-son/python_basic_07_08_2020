"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов.
"""

def my_func(*args):
    vrem_var = 0
    vrem_list = []
    sum = 0
    for each_var in args:
        vrem_list.append(each_var)

    if vrem_list[0] >= vrem_list[1]:
        vrem_var = vrem_list[0]
        if vrem_list[1] >= vrem_list[2]:
            sum = vrem_var + vrem_list[1]
        else:
            sum = vrem_var + vrem_list[2]
    else:
        vrem_var = vrem_list[1]
        if vrem_list[0] >= vrem_list[2]:
            sum = vrem_var + vrem_list[0]
        else:
            sum = vrem_var + vrem_list[2]
    return print(f'Сумма наибольших двух аргументов: {sum}')
