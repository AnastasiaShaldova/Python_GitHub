import decimal
from requests import get, utils



def currency_rates(currency):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    new_content = content.split('<Valute ID=')

    for i in new_content:
        if currency.upper() in i:
            return decimal.Decimal(i.replace('</Value>', '<Value>').split('<Value>')[-2].replace(',', '.'))


if __name__ == '__main__':
    print(currency_rates('USD'))
    print(currency_rates('EUR'))
    print(currency_rates('dgh'))