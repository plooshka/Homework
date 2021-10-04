def number_of_divisors(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count


def prime_numbers(quantity):
    number = 0
    while number <= quantity:
        number += 1
        if number_of_divisors(number) == 2:
            yield number


def goldbach_pair(even_number):
    prime_numbers_list = list(prime_numbers(even_number))
    for i in range(len(prime_numbers_list)):
        for j in range(len(prime_numbers_list)):
            test_sum = prime_numbers_list[i] + prime_numbers_list[j]
            if test_sum == even_number:
                return prime_numbers_list[i], prime_numbers_list[j]
