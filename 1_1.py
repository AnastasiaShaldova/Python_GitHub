duration = int(input('Введите количество секунд: '))
second = duration % 60
minute = (duration // 60) % 60
hour = (duration // 3600) % 24
day = (duration // 86400) % 365
year = duration // 31_536_000

print(f'{year} г(лет) {day} дн {hour} ч {minute} мин {second} сек')