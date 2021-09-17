def tuple_to_int(input_tuple: tuple) -> int:
    string_to_int = str()
    for element in input_tuple:
        string_to_int += str(element)
    return int(string_to_int)


given_tuple = (1, 2, 3, 4, 15, 18, 1,)
print(tuple_to_int(given_tuple))
print(type(tuple_to_int(given_tuple)))
