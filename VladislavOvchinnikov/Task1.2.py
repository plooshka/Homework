import string
from collections import Counter


def number_of_chars(input_str: string):
    return Counter(input_str.lower())


input_from_keybord = input("Type a string:\n")
print(number_of_chars(input_from_keybord))
