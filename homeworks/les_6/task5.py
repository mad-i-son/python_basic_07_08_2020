"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем
атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение
“Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение. Создать
экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    title = ''

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'Рисуем предметом {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Рисуем предметом {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Рисуем предметом {self.title}')


exampl_1 = Pen()
exampl_1.title = 'Ручка'
exampl_1.draw()

exampl_2 = Pencil()
exampl_2.title = 'Карандаш'
exampl_2.draw()

exampl_3 = Handle()
exampl_3.title = 'Маркер'
exampl_3.draw()
