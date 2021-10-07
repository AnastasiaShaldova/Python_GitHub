class MyOwnErr(Exception):
    def __init__(self, divident, divider):
        self.divident = divident
        self.divider = divider

    @staticmethod
    def number(divident, divider):
        try:
            return (divident / divider)
        except:
            return f'Деление на ноль недопустимо'

print(MyOwnErr.number(10, 0))
print(MyOwnErr.number(10, 2))
