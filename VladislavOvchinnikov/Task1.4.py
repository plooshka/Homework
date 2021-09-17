def sort_dict_by_key(input_dict: dict):
    ordered_dict = dict()
    sorted_keys = sorted(input_dict.keys())
    for key in sorted_keys:
        ordered_dict[key] = input_dict[key]
    return ordered_dict


d = {2: 3, 1: 89, 4: 5, 3: 0, 15: 18, 14: 20, 7: 20}
e = {'a': 3, "x": 89, "c": 5, "r": 0, "j": 18, "l": 20, "k": 20}
print(sort_dict_by_key(d))
print(sort_dict_by_key(e))
