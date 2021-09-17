import re
import string


def sorted_words(input_str: string):
    split_string = re.split(', |,', input_str)
    words_set = set(split_string)
    return sorted(words_set)


input_from_keybord = input("Type a string:\n")
print(sorted_words(input_from_keybord))
