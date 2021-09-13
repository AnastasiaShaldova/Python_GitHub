# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе,
# вернуть None. Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.
import decimal
import datetime

from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)
new_content = content.split('<Valute ID=')


def currency_rates(currency):
    for i in new_content:      # i подстрока содержится в списке
        if currency.upper() in i:     #  ищем значение в подстроке i и возвращаем её
            return decimal.Decimal(i.replace('</Value>', '<Value>').split('<Value>')[-2].replace(',', '.')) # заменяем запятую, чтоб получить float и удаляем вокруг
    for i in new_content:
        print(i.replace('Date=', ' name=').split(' name=')[-2].replace('"', ''))
        return




print(currency_rates("AUD"))
print(currency_rates("eur"))
print(currency_rates("Eghgjh"))

