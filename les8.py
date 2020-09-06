import random


class SomeError(Exception):
    def __init__(self, text=''):
        self.text = text


class SomeBase:
    pass


class SingleTone:
    __instance = None

    def __init__(self):
        self.data = random.randint(1, 20)

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance


class SomeIterator:
    def __init__(self, data):
        self.ind = 0
        self.data = data

    def __next__(self):
        self.ind += 1
        if len(self.data) > self.idx:
            return self.data[self.idx - 1]
        raise StopIteration


class Car:
    def __init__(self, name, number = None):
        self.name = name
        self.number = number

class Garage:
    def __init__(self, name):
        self.name = name

    def add_car(self, *cars):
        self.__box.extend(cars)

    def __iter__(self):
        return  self.__box.__iter__()

class CarsFabric:
    def __iter__(self, name, count):
        self.__name = name
        self.__count = count

    def __call__(self, *args, **kwargs):
        if name:
            self.__name = name
        if count:
            self.__count = count

        def create(self):
            result = [Car(f'{self.__name}_{itm}', itm) for itm in range(self.__count)]


if __name__ == '__main__':
    garage = Garage('!CrazyMoney')

a = SingleTone()
b = SingleTone()
print(1)


def some_f(data):
    if data < 3:
        raise SomeError('DATA < 3')
    return data


for n in range(0, 20):
    try:
        some_f(n)
    except SomeError as e:
        print(e)
        some_f(n + 3)

# raise SomeError('SOME TEXT ERROR')
