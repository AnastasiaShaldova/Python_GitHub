from functools import wraps


def val_checker(f):
    def _val_checker_in(func):
        @wraps(func)
        def wrapper(i):
            if f(i):
                print(func(i))
            else:
                raise ValueError(f'wrong val {i}')

        return wrapper

    return _val_checker_in


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


try:
    n = calc_cube(-6)
except (ValueError, TypeError) as e:
    print(e)
