# from sys import argv
#
# def my_sum(*args):
#     return sum(args)
#
# def devisor(a, b):
#     return a / b
#
# menu = {
#     'devisorn': devisor,
#     'sum': my_sum,
# }
#
# _, command, *args = argv
#
# args_is_good = True
# for idx, itm in enumerate(args):
#     try:
#         args[idx] = float(itm)
#     except ValueError:
#         print('Ошибка ввода')
#         args_is_good = not args_is_good
#         break
#
#
# if args_is_good:
#     result = menu[command](*args)
#     print(result)

import time

def some_f(a, b):
    result = 0
    for itm in range(a ** b):
        # time.sleep(2)
        result += (10 * a) ** b
        # print(result)

start_time = time.time()
some_f(3, 5)
print(time.time() - start_time)