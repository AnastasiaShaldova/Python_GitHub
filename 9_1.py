import time


class TrafficLight:

    def __init__(self):
        self.__color_red = 'red'
        self.__color_yellow = 'yellow'
        self.__color_green = 'green'

    def running(self):
        # while True:
        print(f'\033[31m{self.__color_red}')
        time.sleep(7)
        print(f'\033[33m{self.__color_yellow}')
        time.sleep(2)
        print(f'\033[32m{self.__color_green}')
        time.sleep(5)






result = TrafficLight()
result.running()
