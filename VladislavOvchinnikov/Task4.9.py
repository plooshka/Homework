import string
from collections import Counter


def chars_counter(*strings):
    """The function that counts the number of occurrences of letters in words
    and prints the result.
    """
    intersection = list()
    number_of_words = 0
    for elem in strings:
        number_of_words += len(elem)
        for char in string.ascii_lowercase:
            for str in elem:
                if char in str:
                    intersection.append(char)
    unique_chars = Counter(intersection)

    test1_1 = list()
    test1_2 = list()
    test1_3 = list()
    test1_4 = list(string.ascii_lowercase)
    for key, value in unique_chars.items():
        test1_4.remove(key)
        if value == number_of_words:
            test1_1.append(key)
        if value >= 1:
            test1_2.append(key)
        if value >= 2:
            test1_3.append(key)
    print("This char(s) appear in all strings:")
    print(test1_1)
    print("This char(s) appear in at least one string   :")
    print(test1_2)
    print("This char(s) appear in at least two string   :")
    print(test1_3)
    print("Characters of alphabet, that were not used in any string:")
    print(test1_4)


test_strings = ["hello", "world", "python", ]
print(chars_counter(test_strings))
