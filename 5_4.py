src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123] # так должно получиться


# def num():
#     for i in range(1, len(src)):
#         if src[i] > src[i - 1]:
#             yield src[i]
#
#
# print(*num())

num = [src[i] for i in range(1, len(src)) if src[i] > src[i - 1]]
print(num)