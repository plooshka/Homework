import time


def odd_numbers():
    number = 0
    while True:
        if number % 2 != 0:
            yield number
        number += 1
        time.sleep(0.01)


gen = odd_numbers()
while True:
    print(next(gen))