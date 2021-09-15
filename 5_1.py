def gen(n):
    for i in range(1, n):
        if i % 2 == 1:
            yield i


for b in gen(15):
    print(b)
