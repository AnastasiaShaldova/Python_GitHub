class Stationery:
    def __init__(self, title):
        self.title = title

    def __draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title}')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title}')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title}')

pen = Pen('Ручка')
pensil = Pencil('Карандаш')
handle = Handle('Маркер')
pen._Stationery__draw()
pen.draw()
pensil._Stationery__draw()
pensil.draw()
handle._Stationery__draw()
handle.draw()

