import random
import enum


class Modes(enum.Enum):
    celsius = 'C'
    fahrenheit = 'F'
    kelvin = 'K'


class Display:
    def __init__(self, sensor: "Sensor"):
        self.sensor: "Sensor" = sensor

    def view(self):
        print(self.sensor)

    def switch_mode(self, mode):
        self.sensor(mode)


class Temperature:
    __KELVIN_CONST_C = 273.15

    __slots__ = ('kelvin', '__mode')

    def __init__(self):
        self.kelvin = 0
        self.__mode = Modes.kelvin

    @property
    def celsius(self):
        return self.kelvin - self.__KELVIN_CONST_C

    @celsius.setter
    def celsius(self, value):
        if value < -self.__KELVIN_CONST_C:
            raise ValueError('Материя замерзла')
        self.kelvin = value + self.__KELVIN_CONST_C

    @property
    def fahrenheit(self):
        return self.kelvin * 1.8 - 459.67

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.kelvin = (value + 459.67) / 1.8

    def set_mode(self, mode):
        if mode not in Modes:
            raise ValueError('НЕТ ТАКОГО РЕЖИМА')
        self.__mode = mode

    def __str__(self):
        return f'{getattr(self, self.__mode.name)} {self.__mode.value}'


class Sensor:

    def __init__(self):
        self.__temp = Temperature()

    @property
    def data(self) -> "Temperature":
        data = random.randint(-274, 300)
        self.__temp.celsius = data
        return self.__temp

    def __str__(self):
        return self.data.__str__()

    def __call__(self, mode):
        self.__temp.set_mode(mode)


class Data:
    __slots__ = ('data',)

    def __init__(self, data: list = None):
        self.data = data if data else [random.randint(1, 15) for _ in range(4)]

    def __add__(self, other: "Data"):
        result = list(map(sum, zip(self.data, other.data)))
        return Data(result)


if __name__ == '__main__':
    sensor = Sensor()
    display = Display(sensor)
    display.view()

    # d1 = Data()
    # d2 = Data()
    # d3 = d1 + d2
    # d4 = d1.__add__(d2)
    # print(1)