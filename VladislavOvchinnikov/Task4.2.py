def is_palindrome(input_str: str) -> bool:
    """The function that check whether a string is a palindrome or not"""

    straight_string = ""
    for i in input_str:
        if i.isalnum():
            straight_string += i

    reversed_string = ''
    for k in input_str[::-1]:
        if k.isalnum():
            reversed_string += k

    if straight_string == reversed_string:
        return True
    else:
        return False


print(is_palindrome("11/11/11"))
print(is_palindrome("11/11/11 11:11"))
print(is_palindrome("11/11/14 11:11"))
print(is_palindrome("02/02/2020"))
print(is_palindrome("madam"))
print(is_palindrome("racecar"))

