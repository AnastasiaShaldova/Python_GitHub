class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'My name is: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'I earn: {self._income.get("wage") + self._income.get("bonus")}')



result = Position('Leo', 'Green', 'Boss', 15000, 10000)
result.get_full_name()
result.get_total_income()