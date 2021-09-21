def split_by_index(s: str, indexes: list[int]) -> list[str]:
    """The function which splits the string by indexes"""

    start_position_index = 0
    split_string = list()

    for index in indexes:
        if index > len(s)+1:
            continue
        split_string.append(s[start_position_index:index])
        start_position_index = index
    split_string.append(s[start_position_index:])
    return split_string


print(split_by_index("efwewefc  ecewe efqff", [1, 4, 5, 150, 6, 7]))
print(split_by_index("efwewefc  ecewe efqff", [1000]))
