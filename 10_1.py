class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])

    def __add__(self, other):
        return Matrix([[cell_1 + cell_2 for cell_1, cell_2 in zip(row_1, row_2)]
                       for row_1, row_2 in zip(self.matrix, other.matrix)])


matrix_1 = Matrix([[31, 22, 0], [37, 43, 0], [51, 86, 0]])
matrix_2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
print(matrix_1 + matrix_2)
print('-' * 10)
print(matrix_1)
print('-' * 10)
print(matrix_2)