from functools import wraps


def type_logger(func):
    @wraps(func)
    def type_log(*args, **kwargs):
        number = tuple(args or kwargs)
        for i in number:
            print(f'{func.__name__}({i}: {type(i)})')
        return number

    return type_log


@type_logger
def calc_cube(x):
    return x ** 3


calc_cube(2, 3, 1.25, 'asr')
