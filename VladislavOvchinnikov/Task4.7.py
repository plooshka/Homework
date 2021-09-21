def multiply(input_list: list[int]) -> int:
    """The function that multiply all elements in a given list"""
    int_product = 1
    for i in input_list:
        int_product *= i
    return int_product


def foo(input_list: list[int]) -> list[int]:
    """The function which, given a list of integers,
    return a new list such that each element at index i
    of the new list is the product of all the numbers in
    the original array except the one at i
    """
    product_of_all_elements = multiply(input_list)
    product_list = list()
    for i in input_list:
        product_list.append(product_of_all_elements/i)
    return product_list


print(foo([1, 2, 3, 4, 5]))
print(foo([3, 2, 1]))
print(foo([1, 2, 3, 4, 5, 10]))