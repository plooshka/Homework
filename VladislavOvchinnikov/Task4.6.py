import re


def get_longest_word(s: str) -> str:
    """The function which returns the longest word in the given string"""

    longest_word = ""
    words_in_string = s.split(" ")
    for word in words_in_string:
        word = re.sub(r"[\s]", "", word)
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


print(get_longest_word('Python is simple and effective!'))
print(get_longest_word('Anycsqcqcc pythonista like n\\\\am\ae\fspaces\t a lot.'))
print(get_longest_word('Python is simple and effective language for the machine learningggggg!'))
