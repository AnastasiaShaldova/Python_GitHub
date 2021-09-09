def thesaurus(*args):
    names = {}
    for value in sorted(args):
        key = value[0]
        names.setdefault(key, []).append(value)

    return names



print(thesaurus("Иван", "Ян", "Петр", "Илья", "Евгения"))
