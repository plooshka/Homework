from contextlib import suppress


def suppress_decorator(func):
    def wrapper(*args, **kwargs):
        with suppress(BaseException):
            return func(*args, **kwargs)
    return wrapper


@suppress_decorator
def f(*args, **kwargs):
    file = open("afwfw.cvs", "wdfwd")
    file.write("Holy")
    return 1 / 0


f()
