def unique_dict_values(input_list: list) -> set:
    unique_values = set()
    for _dict in input_list:
        for value in _dict.values():
            unique_values.add(value)
    return unique_values


input_list_data = [{"V": "S001"},
                   {"V": "S002"},
                   {"VIII": "S0071"},
                   {"VI": "S001"},
                   {"VI": "S005"},
                   {"VII": "S005"},
                   {"V": "S009"},
                   {"VIII": "S007"},
                   {"VIII": "S0071"},
                   ]
print(unique_dict_values(input_list_data))
