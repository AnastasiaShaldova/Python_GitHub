from itertools import zip_longest
from time import perf_counter
start = perf_counter()

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Ирина', 'Алексей', 'Владимир', 'Роман']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А', '7Д', '8Г']


def groops():
    new = {k: v for v, k in zip_longest(klasses, tutors)}
    print(new)


groops()
print(perf_counter() - start)
