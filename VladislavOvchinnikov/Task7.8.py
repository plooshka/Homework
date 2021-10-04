class MySquareIterator:

    def __init__(self, iterable_obj):
        self.data = iterable_obj

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.data):
            result = self.data[self.n] ** 2
            self.n += 1
            return result
        else:
            raise StopIteration


lst = [1, 2, 3, 4, 5, 6, 7]
itr = MySquareIterator(lst)
for item in itr:
    print(item)
