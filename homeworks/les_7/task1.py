"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
 (метод __init__()), который должен принимать данные (список списков) для
формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в
виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть
новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


def full_matrix(svar_list, ovar_list):
    str_first_matr = len(svar_list)
    row_first_matr = len(svar_list[0])
    str_second_matr = len(ovar_list)
    row_second_matr = len(ovar_list[0])
    max_str = 0
    max_row = 0
    if str_first_matr >= str_second_matr:
        max_str = str_first_matr
    else:
        max_str = str_second_matr

    if row_first_matr >= row_second_matr:
        max_row = row_first_matr
    else:
        max_row = row_second_matr

    matrix_string = []
    for _ in range(max_row):
        full_matr = []
        for _ in range(max_str):
            full_matr.append(0)
        matrix_string.append(full_matr)
    return matrix_string


def add_matrix(svar_list, ovar_list):
    matr_string = []
    for ind_str, elem_str in enumerate(svar_list):
        new_matrix = []
        for ind_row, elem_row in enumerate(elem_str):
            try:
                if not ovar_list[ind_str][ind_row] is None:
                    new_matrix.append(elem_row + ovar_list[ind_str][ind_row])
            except:
                new_matrix.append(elem_row)
        matr_string.append(new_matrix)
    return matr_string


class Matrix:

    def __init__(self, var_list):
        self.var_list = var_list

    def __str__(self):
        result = '#\n'.join(
            [f"{line_idx}#" + str(line)
             for line_idx, line in enumerate(self.var_list, 1)]) + "#"
        count_row = ''
        for ind in range(len(self.var_list[0])):
            count_row += ' #' + str(ind + 1) + '# '
        return f" {count_row}\n" + result + f"\n {count_row}\n"

    def __add__(self, other):
        matrix_string = full_matrix(self.var_list, other.var_list)
        matrix_string = add_matrix(matrix_string, self.var_list)
        matrix_string = add_matrix(other.var_list, matrix_string)
        return matrix_string


user_matrix1 = [[31, 22], [37, 43], [51, 86]]
user_matrix2 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]

matr1 = Matrix(user_matrix1)
# matr2 = Matrix(user_matrix2)

print(matr1)
# print(matr1+matr2)
