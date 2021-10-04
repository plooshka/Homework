import time


class EvenRange:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.n = self.start

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.end:
            if self.start >= self.end:
                raise StopIteration
            self.start = self.n
            self.n += 1
            if self.start % 2 == 0:
                return self.start


er1 = EvenRange(7, 11)
print(next(er1))
print(next(er1))
print(next(er1))
print(next(er1))
print(next(er1))
print(next(er1))
print(next(er1))
print(next(er1))
print(next(er1))
print(next(er1))

er2 = EvenRange(3, 14)
for number in er2:
    time.sleep(0.1)
    print(number)
