import re


def email_parse(user_input):
    try:
        RE_MAIL = re.match(r'(?P<Username>\w+)@(?P<Domian>\w+\.\w+)', user_input)
        return RE_MAIL.groupdict()
    except (TypeError, AttributeError):
        print(f'Check the correctness of the entered e-mail address! ')
        exit(1)

print(email_parse('someone@geekbrains.ru'))