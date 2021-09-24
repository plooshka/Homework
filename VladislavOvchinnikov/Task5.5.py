data_base = list()


def remember_result(func):
    """The decorator which remembers last result of function"""

    def wrapper(*args):
        last_result = None
        if len(data_base) != 0:
            last_result = data_base.pop()
        print("Last result = " + str(last_result))
        result = func(*args)
        data_base.append(result)
        return result
    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        if type(item) == type(result):
            result += item
        else:
            result += str(item)
    print(f"Current result = '{result}'")
    return result


sum_list("a", "b")
sum_list("abc", "cde")
sum_list(3, 4, 5)
sum_list("gggg", "wpwpwp")
