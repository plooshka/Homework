def get_pairs(lst: list) -> list[tuple]:
    """The function which returns a list of tuples containing pairs of elements"""
    if len(lst) == 1:
        return None

    list_of_pairs = list()
    i = 0

    while i != (len(lst)-1):
        print(i)
        pair = (lst[i], lst[i+1])
        list_of_pairs.append(pair)
        i += 1
    return list_of_pairs


print(get_pairs([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_pairs(['need', 'to', 'sleep', 'more']))
print(get_pairs([1]))
