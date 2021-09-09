import random


def get_jokes(n, flag=False):
    """joke generator"""
    for i in range(n):
        if flag == True:
            while i != n:
                zipped = list(zip(random.sample(nouns, n), random.sample(adverbs, n), random.sample(adjectives, n)))
                print(str(zipped))
                return zipped
        else:
            new_list = random.choices(nouns) + random.choices(adverbs) + random.choices(adjectives)
            print(' '.join(new_list))


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

get_jokes(4, True)