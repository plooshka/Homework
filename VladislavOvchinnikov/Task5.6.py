cashed_data = list()


def call_once(func):
    """The decorator which runs a function or method once and caches the result"""

    def wrapper(a, b):
        if len(cashed_data) == 0:
            cashed_data.append(func(a, b))
            return func(a, b)
        else:
            return cashed_data[0]
    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


print(sum_of_numbers(999, 100))
print(sum_of_numbers(13, 42))
print(sum_of_numbers(134, 412))
print(sum_of_numbers(856, 232))
print(sum_of_numbers(0, 0))
