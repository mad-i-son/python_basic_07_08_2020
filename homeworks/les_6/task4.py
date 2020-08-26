"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен
показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed, color, name, is_police):

        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        if self.speed > 0:
            print('Машина поехала')

    def stop(self,speed):
        self.speed = speed
        if self.speed == 0:
            print('Машина остановилась')

    def turn(direction):
        return print(f'Машина повернула')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')

car_1 = TownCar(70, 'White', 'Maseratti', True)
car_2 = TownCar(50, 'Yellow', 'Kia', False)
car_3 = WorkCar(45, 'Red', 'Belarus', False)

car_1.go(90)
car_1.show_speed()
car_1.turn()
car_1.stop(0)

