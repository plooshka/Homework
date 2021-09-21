def split_analog(input_str: str, delimiter=" ", number_of_splits=-1) -> list:
    """The function which works the same as str.split method"""

    start_position_index = 0
    current_position_index = 0
    split_string = list()

    for char in input_str:
        if char == delimiter and number_of_splits != 0:
            split_string.append(input_str[start_position_index:current_position_index])
            start_position_index = current_position_index + 1
            number_of_splits -= 1
        current_position_index += 1
    split_string.append(input_str[start_position_index:])
    return split_string


print(split_analog("wefwe , ewfwefewf,  wefwef , fwe, wefwef", ","))
print(split_analog("wefwe , ewfwefewf,  wefwef , fwe, wefwef", "w", 3))
print(split_analog("wefwe342we ! ewfwefewf,  ?wefwef , !n!  !!fwe, ?wefwef", "!", 2))
print(split_analog("wefwe , ewfwefewf,  wefwef , fwe, wefwef"))
