def generate_squares(num: int) -> dict:
    """The function that takes a number as an argument and returns a dictionary,
    where the key is a number and the value is the square of that number
    """
    dict_of_squares = {}
    for i in range(1, num+1):
        dict_of_squares[i] = i*i
    return dict_of_squares


print(generate_squares(10))
