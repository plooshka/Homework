def get_digits(num: int) -> tuple[int]:
    """The function which returns a tuple of a given integer's digits"""

    list_of_digits = list()
    for digit in str(num):
        list_of_digits.append(int(digit))
    return tuple(list_of_digits)


print(get_digits(1234325666256))
print(get_digits(87178291199))
print(type(get_digits(123456)))
