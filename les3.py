# def some_funk(some_a: float, some_b:float, some_c: int) -> float:
#     """Вычисляет сумму и возводит в степень
#     :param some_a: float первый аргумент
#     :return: float
#     """
#     result = (some_a + some_b) ** some_c
#     return result
#
# test = some_funk(2, 5, 4)
#
# print(some_funk.__doc__)
#
#
# def my_map(func, iter_obj):
#     result = []
#     for itm in iter_obj:
#         result.append(func(itm))
#         return result
#
# # def my_map(func, iter_obj):
# #     for itm in iter_obj:
# #         yield func[itm]
#
# test_list =[2, 3, 4, 5, 6]
# for itm in my_map(my_f, test_list):
#     print(itm)


def my_zip(*args):
    idx = 0
    while True:
        result = []
        try:
            for itm in args:
                result.append(itm[idx])
        except IndexError:
            break
        yield tuple(result)
        idx += 1

list_a = [1,2,3,4]
print(list(my_zip(list_a)))

"""Встроенные функции
map,
sorted,
sum,
min,
max,
zip,
enumerate,
range
reduce
"""