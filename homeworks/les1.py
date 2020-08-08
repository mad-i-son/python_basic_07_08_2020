# Quest_1
var_one = 5
var_two = 4

print(f'Первая переменная - {var_one}')
print(f'Вторая переменная - {var_two}')

var_user_one = input('Введите первую переменную: ')
var_user_two = input('Введите вторую переменную: ')

print(f'Пользователь ввел переменную {var_user_one}, а после переменную {var_user_two}')

# # Quest_2
time = int(input('Введите время в секундах: '))
if time >= 0:
   hours = time // 3600
   minutes = (time - (hours*3600)) // 60
   seconds = (time - (hours*3600) - (minutes*60))
   print(f'Время {hours:02}:{minutes:02}:{seconds:02}')
else:
    print('Введено отрицательное значение, для вычисления времени введите не отрицательное число секунд.')

# # Quest_3
str_n = input('Введите число n: ')
str_n2 = str_n + str_n
str_n3 = str_n + str_n + str_n

int_n = int(str_n)
int_n2 = int(str_n2)
int_n3 = int(str_n3)
summa_user_variable = int_n + int_n2 + int_n3
print(summa_user_variable)

# Quest_4
user_var = int(input('Введите целое положительное число: '))
medium_var = 0
max_var = 0

while user_var:
    medium_var = user_var % 10
    if max_var < medium_var:
        max_var = medium_var
    user_var = user_var // 10

print(max_var)

# Quest_5
proceeds = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))

if proceeds > costs:
    print('Фирма работает с прибылью')
    profitability = ((proceeds - costs) / proceeds ) * 100
    print('Рентабельность фирмы составила: ', format(profitability, '.2f'), '%')
    average_headcount = int(input('Введите численность сотрудников фирмы: '))
    profit_per_employee = (proceeds - costs) / average_headcount
    print(f'Прибыль на одного сотрудника составила: {"%.2f" %profit_per_employee}')
else:
    print('Фирма убыточна')

# Quest_6
a = int(input('Введите результат спортсмена за первый день: '))
b = int(input('Введите результат спортсмена на который он ровняется: '))
day = 1

while a < b:
     a = a * 1.1
     day += 1
else:
    print(f'на {day}-й день спортсмен достиг результата - не менее {b} км.')