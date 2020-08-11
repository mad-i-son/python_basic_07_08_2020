var_list = []
new_var_list = []
while True:
    user_list = input('Введите число для списка: ')
    try:
        if user_list.isdigit():
            var_list.append(int(user_list))
        else:
            print('Было введено не число, попробуйте ещё раз или покинте программу.')
    except ValueError:
        continue

    user_anwer = input('Если чисел достаточно, то введите Y, если нет то N: ')

    try:
        if user_anwer.isalpha():
            if user_anwer == 'Y':

                new_var_list = var_list[:]

                count = len(new_var_list)
                if count > 0 and count % 2 == 0:
                    index_var = 0
                    second_var = 0
                    for each_var in new_var_list:
                        index_var += 1
                        if index_var <= count and index_var % 2 == 1:
                            second_var = new_var_list[index_var]
                            new_var_list[index_var] = each_var
                            new_var_list[index_var-1] = second_var
                    print(f'Первоначальный спискок {var_list} и новый список {new_var_list}')
                elif count > 0 and count % 2 == 1:
                    index_var = 0
                    second_var = 0
                    for each_var in new_var_list:
                        index_var += 1
                        if index_var < count and index_var % 2 == 1:
                            second_var = new_var_list[index_var]
                            new_var_list[index_var] = each_var
                            new_var_list[index_var - 1] = second_var
                    print(f'Первоначальный спискок {var_list} и новый список {new_var_list}')
                elif count == 0:
                    print('Список пуст сортировать нечего.')

                break
            elif user_anwer == 'N':
                pass
            else:
                print('Введено значение не влияющее на работу')
    except ValueError:
        continue

