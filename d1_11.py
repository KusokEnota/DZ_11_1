"""Создайте класс Матрица. Добавьте методы для: - вывода на печать,
сравнения,
сложения,
*умножения матриц"""


class Matrix:
    def __init__(self, matr):
        self._matr = matr

    def get_matrix(self):
        return self._matr

    def __add__(self, other):
        return Matrix([[self._matr[i][j] + other._matr[i][j] for j in range(len(self._matr[0]))] for i in
                       range(len(self._matr))]) if self._check_dimensions(other) else f'Матрицы разных размеров !'

    def __mul__(self, other):
        if len(self._matr[0]) != len(other._matr):
            return f'Невозможно перемножить матрицы!'
        return Matrix([[sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*other._matr)] for
                       i_row in self._matr])

    def __eq__(self, other):
        if not self._check_dimensions(other):
            return f'Матрицы разных размеров!'
        return all(self._matr[i][j] == other._matr[i][j] for i in range(len(self._matr)) for j
                   in range(len(self._matr[0])))

    def __str__(self):
        return '\n'.join([str(row) for row in self._matr])

    def _check_dimensions(self, other):
        return len(self._matr) == len(other._matr) and len(self._matr[0]) == len(other._matr[0])


m_1 = [[1, 2, 4],
       [5, 6, 8],
       [2, 5, -2],
       [10, 5, 0]]

m_2 = [[1, 2, 4],
       [5, 6, 8],
       [5, 6, 8],
       [-2, 2, 0]]

m_3 = [[1, 2, 4, 5],
       [5, 6, 8, 0],
       [5, 0, -7, 1]]

m_4 = [[1, 2, 4, 5, 0],
       [5, 6, 8, 0, 0],
       [5, 0, -7, 1, 0]]

matr_1 = Matrix(m_1)
matr_2 = Matrix(m_2)
matr_3 = Matrix(m_3)
matr_4 = Matrix(m_4)

print("Сравнение матриц:")
print(matr_1 == matr_1)
print(matr_1 == matr_2)

print("Сложение матриц:")
matr_sum = matr_1 + matr_2
print(matr_sum)

print("Умножение матриц:")
matr_mul = matr_1 * matr_3
print(matr_mul)
print(matr_1 * matr_4)
