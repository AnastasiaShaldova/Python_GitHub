class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date):
        day, month, year = map(int, date.split('-'))
        return f'Дата: {day}\nМесяц: {month}\nГод: {year}'

    @staticmethod
    def is_date_valid(date):
        day, month, year = map(int, date.split('-'))
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2021:
                    return f'Корректная дата: {date}'
                else:
                    return f'Некорректный год: {year}'
            else:
                return f'Неккоректный месяц: {month}'
        else:
            return f'Неккоректный день: {day}'


date1 = Date.from_string('06-10-2021')
print(date1)
date2 = Date.is_date_valid('06-10-2021')
print(date2)
date3 = Date.is_date_valid('41-10-2021')
print(date3)
date4 = Date.is_date_valid('06-13-2021')
print(date4)
date5 = Date.is_date_valid('06-10-2028')
print(date5)

