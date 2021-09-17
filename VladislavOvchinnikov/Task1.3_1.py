def all_divisors(number: int):
    divisors = list()
    for divisor in range(1, number+1):
        if number % divisor == 0:
            divisors.append(divisor)
    return divisors


input_int = int(input("Type a integer:\n"))
print(all_divisors(input_int))
