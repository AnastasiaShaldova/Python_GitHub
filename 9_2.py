class Road:

    def __init__(self, l, w, d=5):
        self._length = l
        self._width = w
        self.depth = d

    def canvas(self):
        road_surface = self._length * self._width * 0.025 * self.depth
        print(f'масса для покрытия всего полотана: {road_surface} т.')


result = Road(10, 100, 5)
result.canvas()
