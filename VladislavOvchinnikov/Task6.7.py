class Money:

    exchange_rate = {
        "EUR": 3.0,
        "USD": 2.5,
        "JPY": 0.02,
        "BYN": 1,
    }

    def __init__(self, value, currency="BYN"):
        self.value = value
        self.currency = currency

    def __eq__(self, other):
        return self.currency == other.currency

    def __lt__(self, other, exchange_rate=exchange_rate):
        if self.__eq__(other):
            return self.value < other.value
        else:
            return self.value < other.value * exchange_rate[other.currency]

    def __mul__(self, other, exchange_rate=exchange_rate):
        if type(other) is Money:
            return Money(
                (self.value * exchange_rate[self.currency]) *
                (other.value * exchange_rate[other.currency])
            )
        else:
            return Money((self.value * exchange_rate[self.currency]) * float(other))

    def __rmul__(self, other):
        return Money.__mul__(self, other)

    def __truediv__(self, other, exchange_rate=exchange_rate):
        if type(other) is Money:
            return Money(
                (self.value * exchange_rate[self.currency]) /
                (other.value * exchange_rate[other.currency])
            )
        else:
            return Money((self.value * exchange_rate[self.currency]) / float(other))

    def __rtruediv__(self, other):
        return Money.__truediv__(self, other)

    def __add__(self, other, exchange_rate=exchange_rate):
        if type(other) is Money:
            return Money(
                self.value * exchange_rate[self.currency] +
                other.value * exchange_rate[other.currency]
            )
        else:
            return Money((self.value * exchange_rate[self.currency]) + float(other))

    def __radd__(self, other):
        return Money.__add__(self, other)

    def __sub__(self, other, exchange_rate=exchange_rate):
        if type(other) is Money:
            return Money(
                self.value * exchange_rate[self.currency] -
                other.value * exchange_rate[other.currency]
            )
        else:
            return Money((self.value * exchange_rate[self.currency]) - float(other))

    def __rsub__(self, other):
        return Money.__sub__(self, other)

    def convert_to_usd(self, exchange_rate=exchange_rate):
        return Money(self.value / exchange_rate["USD"], "USD")

    def convert_to_eur(self, exchange_rate=exchange_rate):
        return Money(self.value / exchange_rate["EUR"], "EUR")

    def __repr__(self):
        return f"This is {self.value} of {self.currency}"


x = Money(10, "USD")
y = Money(11)
z = Money(12.34, "EUR")

print(z + 3.11 * x + y * 0.8)

lst = [Money(10, "BYN"), Money(11), Money(2, "USD"), Money(2, "EUR")]
s = sum(lst)
print(s)
print(s.convert_to_usd())
print(s.convert_to_eur())

