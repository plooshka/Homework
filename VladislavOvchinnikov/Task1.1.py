import string


def str_len(input_str: string) -> int:
    i = 0
    for char in input_str:
        i += 1
    return i


string = input("Type any string: \n")
print(str_len(string))
print(len(string))