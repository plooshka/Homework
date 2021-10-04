import time


def endless_fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


gen = endless_fib_generator()
while True:
    print(next(gen))
    time.sleep(0.2)