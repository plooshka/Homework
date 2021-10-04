class NotEvenExeption(ArithmeticError):
    def __init__(self, message):
        self.message = message


class DataTypeExeption(TypeError):
    def __init__(self, message):
        self.message = message


class ValidateExeption(ValueError):
    def __init__(self, message):
        self.message = message


def number_of_divisors(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count


def prime_numbers(quantity):
    number = 0
    while number <= quantity:
        number += 1
        if number_of_divisors(number) == 2:
            yield number


def goldbach_pair(even_number):
    prime_numbers_list = list(prime_numbers(even_number))
    for i in range(len(prime_numbers_list)):
        for j in range(len(prime_numbers_list)):
            test_sum = prime_numbers_list[i] + prime_numbers_list[j]
            if test_sum == even_number:
                return prime_numbers_list[i], prime_numbers_list[j]


def check(a: int) -> bool:
    if a == 'q':
        print("Finish program!")
        return

    if type(a) is not int:
        raise DataTypeExeption(f"Wrong data type! a is {type(a)} , must be int")

    if a % 2 == 0:

        if a > 2:
            return True
        else:
            raise ValidateExeption("Number is less than two!")

    else:
        raise NotEvenExeption("Number is not even!")
        return False


keyboard_input = ""
while keyboard_input != 'q':
    keyboard_input = input("Enter the even number that greater than 2: ")
    if keyboard_input.isdigit():
        keyboard_input = int(keyboard_input)
        print(goldbach_pair(keyboard_input))
    try:
        check(keyboard_input)
    except Exception as err:
        print(err)
