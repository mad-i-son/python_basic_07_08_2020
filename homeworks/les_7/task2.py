"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь
определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для
костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих
методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на
этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod



class Clothes(ABC):
    def __init__(self, cloth):
        self.cloth = cloth

    @abstractmethod
    def metod_clothes(self):
        pass

    def __add__(self, other):
        return f'Расхода ткани всего составил: {self.cloth + other.cloth}'


class Coat(Clothes):
    v = 0

    def __init__(self, v):
        self.v = v

    @property
    def metod_clothes(self):
        clothes_for_coat = self.v / 6.5 + 0.5
        return clothes_for_coat


class Costume(Clothes):
    h = 0

    def __init__(self, h):
        self.h = h

    @property
    def metod_clothes(self):
        clothes_for_coat = 2 * self.h + 0.3
        return clothes_for_coat


coat_1 = Coat(44)
costume_1 = Costume(45)
print(coat_1.metod_clothes)
print(costume_1.metod_clothes)

print(f'Расхода ткани всего составил: {coat_1.metod_clothes + costume_1.metod_clothes}')
