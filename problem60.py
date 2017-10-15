# https://projecteuler.net/problem=60

from utilities import *


def sorted_unique_points(dim):
    unique_point = serial_cube_uniques(dim)

    sorted_points = []
    curr_sum = 0
    while True:
        point = sorted(next(unique_point))
        if point in sorted_points:
            continue
        sorted_points.append(point)
        yield point
        if sum(point) != curr_sum:
            sorted_points = []
            curr_sum += 1


# list of whether or not two prime concatenate. Entry a contains primes>=a
known_concats = {}


def concat_primes(num1, num2):
    num1, num2 = sorted((num1, num2))

    if num1 in known_concats:
        if num2 in known_concats[num1]:
            return known_concats[num1][num2]
        else:
            known_concats[num1][num2] = is_prime(num1 * (10 ** ceil(log10(num2))) + num2) \
                                    and is_prime(num2 * (10 ** ceil(log10(num1))) + num1)
    else:
        known_concats[num1] = {}
        known_concats[num1][num2] = is_prime(num1 * (10 ** ceil(log10(num2))) + num2) \
                                and is_prime(num2 * (10 ** ceil(log10(num1))) + num1)

    return known_concats[num1][num2]


def concat_prime_list(prime_list):
    """
    Determines if all sets of 2 primes in prime_list can be concatenated in either order to form a prime.

    :param prime_list: list of primes to be checked
    :return: boolean
    """
    for c in range(0, len(prime_list)):
        for a in range(0, len(prime_list)):
            if c == a:
                continue
            else:
                if not concat_primes(prime_list[a], prime_list[c]):
                    return False
    return True


primes = PrimeList()

# for i in range(0, 10000):
#     prime1 = primes[i]
#     for a in range(0, 1000):
#         prime2 = primes[a]
#         for b in range(0, 100):
#             prime3 = primes[b]
#             concatable = concat_prime_list([3, 7, prime1, prime2, prime3])
#             if concatable:
#                 print("********************")
#                 print(sum([3, 7, prime1, prime2, prime3]))
#                 exit()
#     print(i)


for i in range(4):
    for a in range(4):
        concat_primes(primes[i], primes[a])
print(known_concats)


# print(is_prime(25241))
# baseList = [3, 7, 109, 673, 0]
# i = 0
# while not concat_primes(baseList):
#     baseList[-1] = primes[i]
#     print(baseList)
#     i += 1
# print(baseList)

# 26033
