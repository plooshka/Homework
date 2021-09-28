from collections import deque


class HistoryDict(dict):

    def __init__(self, val=None):
        if val is None:
            val = {}
        super().__init__(val)
        self.history = deque(maxlen=10)

    def set_value(self, item, value):
        super().__setitem__(item, value)
        self.history.append(item)

    def get_history(self):
        return self.history


d = HistoryDict({"foo": 42})
d.set_value("bar1", 43)
d.set_value("foo2", 42)
d.set_value("zoo3", 41)
d.set_value("barak4", 40)
d.set_value("fooak5", 39)
d.set_value("zooak6", 38)
d.set_value("baron7", 37)
d.set_value("fooon8", 36)
d.set_value("zooon9", 35)
d.set_value("barin10", 34)
d.set_value("fooin11", 33)
d.set_value("zooin12", 32)
d.set_value("zooq13", 31)
print(d.get_history())
print(d)

