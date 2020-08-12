# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к
# какому времени года относится месяц (зима, весна, лето, осень). Напишите
# решения через list и через dict.

while True:
    try:
        month = input('Введите месяц цифрой от 1 до 12: ')
        if month.isdigit():
            month_var = int(month)
            if month_var >= 1 and month_var <= 12:
                break
            else:
                print('Ввдено число отличное от диапазлна 1 до 12, попробуйте ещё раз.')
        else:
            print('Введено не число, попрубйте ещё раз.')
    except ValueError:
        continue

var_list = ['зима', 'весна', 'лето', 'осень']

if (month_var >= 1 and month_var <= 2) or month_var == 12:
    print(f'Введеный месяц соответ времени года - {var_list[0]}')
elif month_var >= 3 and month_var <= 5:
    print(f'Введеный месяц соответ времени года - {var_list[1]}')
elif month_var >= 6 and month_var <= 8:
    print(f'Введеный месяц соответ времени года - {var_list[2]}')
elif month_var >= 9 and month_var <= 11:
    print(f'Введеный месяц соответ времени года - {var_list[3]}')

var_dict = {1: 'зима', 2: 'зима',
            3: 'весна', 4: 'весна', 5: 'весна',
            6: 'лето', 7: 'лето', 8: 'лето',
            9: 'осень', 10: 'осень', 11: 'осень',
            12: 'зима'}

print(f'Введеный месяц соответ времени года - {var_dict[month_var]}')
