prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90, 70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]


for i, n in enumerate(prices):
    penny = int(n * 100)
    print(f'{int(n)} руб. {str(penny)[-2:]} коп.,')

print(id(prices))
prices.sort()
print(prices)
print(id(prices))

copy_prices = list(prices)
copy_prices.sort(reverse=True)
print(copy_prices)
print(id(copy_prices))

prices.sort()
print(prices[-5:])

