class MyError(Exception):
    def __init__(self, text):
        self.txt = text


my_list = []
while True:
    try:
        number_input = input('Введите значание: ')
        print('Для выхода введите "stop"')
        if number_input == 'stop':
            break
        if not number_input.isdigit():
            raise MyError(number_input)
        my_list.append(int(number_input))
    except (ValueError, MyError):
        print('Ведено неверное значение')
print(f'Список: {my_list}')

