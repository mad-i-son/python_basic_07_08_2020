"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Последний атрибут должен
быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
на базе класса Worker. В классе Position реализовать методы получения полного
имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {}

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        result = 0.0
        for var in self._income.values():
            result += float(var)
        return result


rab = Position('Иван', 'Иванов', 'дворник', {"wage": 10000, "bonus": 2000})
print(f'Полное имя сотрудника: {rab.get_full_name()}')
print(f'Доход с учетом премии: {rab.get_total_income()}')

