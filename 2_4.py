fellow_worker = ['инжинер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in fellow_worker:
    worker = i.split()[-1]
    print(f'Привет, {worker.capitalize()}!')

