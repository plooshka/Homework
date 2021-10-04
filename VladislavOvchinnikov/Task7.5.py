class NotEvenExeption(ArithmeticError):
    def __init__(self, message):
        self.message = message


class DataTypeExeption(TypeError):
    def __init__(self, message):
        self.message = message


class ValidateExeption(ValueError):
    def __init__(self, message):
        self.message = message


def check(a: int) -> bool:
    if type(a) is not int:
        raise DataTypeExeption("Wrong data type!")

    if a % 2 == 0:

        if a > 2:
            return True
        else:
            raise ValidateExeption("Number is less than two!")

    else:
        raise NotEvenExeption("Number is not even!")
        return False


try:
    print(check(4))
except Exception as err:
    print(err)

try:
    print(check(9))
except Exception as err:
    print(err)

try:
    print(check(0))
except Exception as err:
    print(err)

try:
    print(check("str"))
except Exception as err:
    print(err)