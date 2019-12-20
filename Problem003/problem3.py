# The prime factors of 13195 are 5, 7, 13 and 29.


def get_prime(number):
    factor = 2
    while factor < number:
        remainder = number % factor
        if remainder == 0:
            prime = factor
            return prime, remainder
        factor = factor + 1
prime, factor
# What is the largest prime factor of the number 600851475143 ?