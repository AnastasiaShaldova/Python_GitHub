class Warehouse:
    def __init__(self):
        self.dict = {}


class OfficeEquipment:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = str(model)
        self.year = year

    def __str__(self):
        return f'Производитель: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.year}'


class Printer(OfficeEquipment):
    def __init__(self, brand, model, year, print_speed):
        super().__init__(brand, model, year)
        self.print_speed = print_speed

    def action(self):
        return f'Печатает'


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, year, scan_quality):
        super().__init__(brand, model, year)
        self.scan_quality = scan_quality

    def action(self):
        return f'Сканирует'


class Xerox(OfficeEquipment):
    def __init__(self, brand, model, year, copy_speed):
        super().__init__(brand, model, year)
        self.copy_speed = copy_speed

    def action(self):
        return f'Копирует'


