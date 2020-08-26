"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина),
width (ширина). Значения данных атрибутов должны передаваться при создании
экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы
асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self.result = 0
        self._length = length
        self._width = width

    def road_work(self, weight, height):
        self.weight = weight
        self.height = height
        self.result = (self._length * self._width * self.weight * self.height) / 1000
        return self.result


road_steet = Road(20, 5000)
print(f' масса асфальта, необходимого для покрытия всего дорожного полотна: {road_steet.road_work(25, 5)} тонн')
