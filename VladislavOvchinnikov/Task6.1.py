class Counter:

    def __init__(self, start_value=0, stop_value=-1):
        self.start_value = start_value
        self.stop_value = stop_value

    def increment(self):
        try:
            if self.stop_value == -1 or self.start_value < self.stop_value:
                self.start_value += 1
            else:
                raise Exception("Maximal value is reached")
        except Exception as e:
            print(e)

    def get(self):
        return self.start_value


c = Counter(start_value=42)
c.increment()
print(c.get())


c = Counter()
c.increment()
print(c.get())

c.increment()
print(c.get())

c = Counter(start_value=42, stop_value=43)
c.increment()
print(c.get())

c.increment()
print(c.get())

c = Counter(start_value=44, stop_value=45)
print(c.get())
c.increment()
c.increment()
print(c.get())
