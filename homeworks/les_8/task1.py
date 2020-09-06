"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в
 виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
  Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
  преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен
   проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
    Проверить работу полученной структуры на реальных данных.
"""


class Date:

    def __init__(self, dat):
        self.dat = dat

    @classmethod
    def extract(cls, dat_str):
        list_date = dat_str.split('-')
        day = int(list_date[0])
        month = int(list_date[1])
        year = int(list_date[2])
        return day, month, year

    @staticmethod
    def validation(day, month, year):
        if day > 0 and day <= 31:
            if month > 0 and month <= 12:
                if year > 0 and year < 2100:
                    print('Валидация пройдена')
                else:
                    print('Ваидация не пройдена.')
            else:
                print('Ваидация не пройдена.')
        else:
            print('Ваидация не пройдена.')


date1 = Date("02-09-3020")
d, m, y = Date.extract(date1.dat)
Date.validation(d, m, y)
