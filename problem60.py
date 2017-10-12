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


def concat_primes(prime_list):
    for c in range(0, len(prime_list)):
        for a in range(0, len(prime_list)):
            if c == a:
                continue
            else:
                if not is_prime(int(str(prime_list[c]) + str(prime_list[a]))):
                    return False
                if not is_prime(int(str(prime_list[a]) + str(prime_list[c]))):
                    return False
    return True


primes = PrimeList()
b = 0
for i in sorted_unique_points(5):
    if b % 5000 == 0:
        print(sum(i), [primes[a] for a in i])
    if concat_primes([primes[a] for a in i]):
        print(b, [primes[a] for a in i], sum([primes[a] for a in i]))
        break
    # if i == [2, 4, 28, 121]:  # 155
    #     break
    b += 1

# print(is_prime(25241))
# baseList = [3, 7, 109, 673, 0]
# i = 0
# while not concat_primes(baseList):
#     baseList[-1] = primes[i]
#     print(baseList)
#     i += 1
# print(baseList)

# 26033
