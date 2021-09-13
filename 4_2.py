import decimal
from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)
new_content = content.split('<Valute ID=')


def currency_rates(currency):
    for i in new_content:
        if currency.upper() in i:
            return float(i.replace('</Value>', '<Value>').split('<Value>')[-2].replace(',', '.'))


print(currency_rates('USD'))
print(currency_rates('Eur'))
print(currency_rates('dgh'))