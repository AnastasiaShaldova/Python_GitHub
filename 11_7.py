class ComplexNumbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сложение комплексных чисел')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Умножение комплексных чисел')
        return f'z = {self.a * other.a - self.b * other.b}*{self.b * other.a + self.a * other.b} * i'


a = ComplexNumbers(1, -2)
b = ComplexNumbers(3, 4)
print(a + b)
print(a * b)