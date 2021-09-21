def combine_dicts(*dicts) -> dict:
    """The function, that receives changeable number of dictionaries
    and combines them into one dictionary
    """
    combined_dict = dict()
    for dictionary in dicts:
        for key, value in dictionary.items():
            if key in combined_dict.keys():
                combined_dict[key] = value + combined_dict[key]
            else:
                combined_dict[key] = value
    return combined_dict


dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}
dict_4 = {'a': 100, 'd': 100, 'e': 5}

print(combine_dicts(dict_1, dict_2))
print(combine_dicts(dict_1, dict_2, dict_3))
print(combine_dicts(dict_1, dict_2, dict_3, dict_4))
