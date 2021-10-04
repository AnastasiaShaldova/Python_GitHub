from abc import ABC


class Garments(ABC):
    def __init__(self, the_size, height):
        self.the_size = the_size
        self.height = height

    @property  # общий расчет ткани
    def total_tissue_area(self):
        return f'Общая площадь ткани: {(self.the_size / 6.5 + 0.5) + (2 * self.height + 0.3)}'


class Coat(Garments):  # расчет ткани на пальто
    def __init__(self, the_size, height):
        super().__init__(the_size, height)
        self.square_coat = round(self.the_size / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь ткани на пальто: {self.square_coat}'


class Costume(Garments):  # расчет ткани на костюм
    def __init__(self, the_size, height):
        super().__init__(the_size, height)
        self.square_costume = round(2 * self.height + 0.3)

    def __str__(self):
        return f'Расход ткани на костюм: {self.square_costume}'


coat = Coat(48, 170)
costume = Costume(44, 150)
print(coat)
print(costume)
print(coat.total_tissue_area)

