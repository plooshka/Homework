from contextlib import contextmanager


@contextmanager
def open_file(filename, method):
    try:
        file = open(filename, method)
        yield file
    except Exception as err:
        print(err)
    finally:
        file.close()


with open_file("text.txt", "r") as file:
    print(file.read())
