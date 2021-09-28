class Bird:

    def __init__(self, name):
        self.name = name

    def fly(self):
        return f"{self.name} can fly"

    def walk(self):
        return "Any bird can walk"

    def __str__(self):
        return f"{self.name} bird can walk"


class FlyingBird(Bird):

    def __init__(self, name, ration="worms"):
        Bird.__init__(self, name)
        self.ration = ration

    def eat(self):
        return f"{self.name} eats mostly {self.ration}"

    def __str__(self):
        return f"{self.name} can walk and fly"


class NonFlyingBird(Bird):

    def __init__(self, name, ration="fish"):
        Bird.__init__(self, name)
        self.ration = ration

    def swim(self):
        return f"{self.name} bird can swim"

    def fly(self):
        raise AttributeError(f"{self.name} object has no attribute 'fly'")

    def eat(self):
        return f"{self.name} eats mostly {self.ration}"

    def __str__(self):
        return f"{self.name} can walk and swim"


class SuperBird(FlyingBird, NonFlyingBird):

    def __str__(self):
        return f"{self.name} can walk, fly and swim under water"


b = Bird("Any")
print(b.walk())

try:
    p = NonFlyingBird("Penguin", "fish")
    print(p.swim())
    print(p.fly())
    print(p.eat())
except Exception as e:
    print(e)

c = FlyingBird("Canary")
print(str(c))
print(c.eat())

s = SuperBird("Gull")
print(str(s))
print(s.eat())
print(SuperBird.__mro__)
