class Cell:
    def __init__(self, cell):
        self.cell = int(cell)

    def __str__(self):
        return f'{self.cell * "*"}'

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        return Cell(self.cell - other.cell) if (self.cell - other.cell) > 0 else print('Вычитание невозможно')

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell / other.cell)

    def make_order(self, row):
        result = ''
        for i in range(int(self.cell / row)):
            result += f'\n{"*" * row}'
        result += f'\n{"*" * (self.cell % row)}'
        return result


cell_1 = Cell(13)
cell_2 = Cell(5)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))
print(cell_2.make_order(3))
