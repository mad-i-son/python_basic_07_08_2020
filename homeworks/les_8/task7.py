"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс
«Комплексное число», реализуйте перегрузку методов сложения и умножения
комплексных чисел. Проверьте работу проекта, создав экземпляры класса
(комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class ComplexNumber:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'z = {(self.a + other.a)} + {(self.b + other.b)}i'

    def __mul__(self, other):
        return f'z = {((self.a * other.a) - (self.b * other.b))} + {((self.b * other.a) + (self.a * other.b))}i'


examp_complex_1 = ComplexNumber(2, 3)
examp_complex_2 = ComplexNumber(4, 5)

print(f' Сумма комплексных чисел ровна: {examp_complex_1 + examp_complex_2}')
print(f' Произведение комплексных чисел ровна: {examp_complex_1 * examp_complex_2}')
