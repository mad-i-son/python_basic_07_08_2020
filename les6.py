class Animal:
    __population = []
    color = ''
    carnivorous = False
    _weight = 0

    def __init__(self, color, carnivorous):

        self.color = color
        self.carnivorous = carnivorous
        Animal.__population.append(self)

    def say(self):

        if self.carnivorous:
            print('RRRRRRRRRRRR')
        else:
            print('MuuuuuuMuuu')


# an1 = Animal()
# an1.carnivorous = False
# an1.weight = 100
# an1.color = 'RED'
#
# an2 = Animal()
# an2.color = 'White'


class Human(Animal):

    def __init__(self, name, color):
        self.name = name
        super().__init__(color, True)

    def breeding(self, other):
        if isinstance(other, Human):
            child = Human(self.name, other.color)
        return child

    def say(self):
        print(f'Hello my name is {self.name}')

    def get_population(self):
        return tuple(self.__population)


class Mystery:
    def __init__(self, phobia, power):
        self.phobia = phobia
        self.power = power

    def work(self):
        print('Im Work')


class Vampire(Human, Mystery):
    def __init__(self, name):
        super().__init__(name, 'Black')
        Mystery.__init__(self, 'Immortal', 'SUN')

    def say(self):
        super().say()
        Mystery.say(self)


vamp = Vampire('Allukard')
hu1 = Human('Vasya', 'Red')
hu2 = Human('Masha', 'Red')
hu3 = hu1.breeding(hu2)

an3 = Animal('Black', False)
an4 = Animal('Blue', True)

print(an3.say())
