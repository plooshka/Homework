class Validator:

    @staticmethod
    def validate_iterable(iterable):
        for i in iterable:
            if type(i) is not int and type(i) is not float:
                raise AttributeError
                return False
        return True

    @staticmethod
    def validate_args(a, b, c):
        if isinstance(a, (tuple, list, set)) and b == None and c == None:
            return True
        if type(a) is not int and type(a) is not float:
            raise AttributeError
            return False
        if type(b) is not int and type(b) is not float:
            raise AttributeError
            return False
        if type(c) is not int and type(c) is not float:
            raise AttributeError
            return False
        return True

    @staticmethod
    def validate_number(insert_data):
        if isinstance(insert_data, (int, float)):
            return True
        return False


class MyNumberCollectionBuilder:

    def __init__(self):
        pass

    def build_collection(self, start, end=None, step=None):
        if Validator.validate_args(start, end, step):
            values = list()
            if isinstance(start, (tuple, set, list)):
                for e in start:
                    values.append(e)
            else:
                values = list(range(start, end, step))
                if end not in values:
                    values.append(end)
        if Validator.validate_iterable(values):
            return MyNumberCollection(values)


class MyNumberCollection:

    def __init__(self, a):
        self.list = list(a)

    def append(self, insert_data):
        if not Validator.validate_number(insert_data):
            raise AttributeError
        else:
            self.list.append(insert_data)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.list):
            result = self.list[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

    def __add__(self, other):
        for elem in other.list:
            if Validator.validate_number(elem):
                self.list.append(elem)
        return MyNumberCollection(self.list)

    def __getitem__(self, item):
        return self.list[item] ** 2

    def __repr__(self):
        return f"{self.list}"


builder = MyNumberCollectionBuilder()
col1 = builder.build_collection((1, 2, 3, 4, 5))
print(col1)
col2 = builder.build_collection(1, 8, 3)
print(col2)
col3 = builder.build_collection((1, 2, 3, 4))
print(col3)
print(col2 + col3 + col1)
print(col1[4])
for item in col1:
    print(item)
