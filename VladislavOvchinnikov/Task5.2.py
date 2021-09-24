import re
from collections import Counter


def most_common_words(filepath: str, number_of_words=3) -> Counter:
    """The function which search for most common words in the file"""

    words = list()
    file = open(filepath, "r")
    data = file.read()
    for word in data.split():
        word = re.sub(r"[\W]", "", word).lower()
        words.append(word)
    file.close()
    return Counter(words).most_common(number_of_words)


print(most_common_words('lorem_ipsum.txt'))
