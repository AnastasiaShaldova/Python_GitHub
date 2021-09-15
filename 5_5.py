import time
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

start = time.perf_counter()
def num():
    for n in src:
        if src.count(n) == 1:
            yield n


finish = time.perf_counter()
print(*num(), finish - start, 'def')


start = time.perf_counter()
unique_num = set()
result = set()
for i in src:
    if i in result:
        unique_num.discard(i)
    else:
        unique_num.add(i)
    result.add(i)

print(unique_num)

unique_num_ord = [i for i in src if i in unique_num]
finish = time.perf_counter()
print(unique_num_ord, finish - start, 'for in')
