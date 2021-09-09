def num_translate():
    user_input = str(input('Enter a number from 0 to 10 in English: '))
    if user_input.istitle():
        return print(dictionary.get(user_input.lower()).title())
    print(dictionary.get(user_input))


dictionary = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
              'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
num_translate()



