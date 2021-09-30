import random

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self._direction = ['на право', 'на лево', 'во двор', 'в лес', 'к озеру']

    def go(self):
        print(f'Едет {self.name} ')

    def stop(self):
        print(f'{self.name} уже не едет')

    def turn(self):
        print(f'{self.color} автомобиль {self.name} проехал красный сигнал светофора и свернул {random.choice(self._direction)}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name}: {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 61:
            print(f'У автомобиля {self.name} скорость движения выше 60 км/ч')
        else:
            print(f'Автомобиль {self.name} соблюдает ПДД')


class SportCar(Car):
    pass


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'У автомобиля {self.name} скорость движения выше 40 км/ч')
        else:
            print(f'Послушный {self.name}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def PoliceAuto(self):
        if self.is_police:
            print(f'{self.name} полицейская машина')
        else:
            print(f'{self.name} не из полиции')


ford = PoliceCar(100, 'Blue', 'Ford', True)
kia = WorkCar(60, 'Green', 'KIA', False)
reno = TownCar(60, 'Red', 'Reno', False)

ford.go()
ford.PoliceAuto()
ford.show_speed()
ford.turn()
ford.stop()
print('<------------------>')
kia.go()
kia.show_speed()
kia.turn()
kia = Car(60, 'Green', 'KIA', False)
kia.show_speed()
kia.stop()
print('<------------------>')
reno.go()
reno.show_speed()
reno.turn()
reno = Car(60, 'Red', 'Reno', False)
reno.show_speed()
reno.stop()