def gen(n):
    gen_res = [i for i in range(1, n) if i % 2 == 1]
    print(*gen_res)


gen(10)
