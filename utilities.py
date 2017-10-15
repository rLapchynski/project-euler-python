
from math import *


def is_prime(num, negative_prime=True):
    """Determines is a number is prime

       If negativePrime==True (default: True), then negative numbers can be prime
    """
    if negative_prime:
        num = abs(num)

    a = factors(num, True)
    return a != [] and a[0] == num


def factors(num, primality_test=False):
    """Determines the prime factors of a number

       If primalityTest==True (default: False), it will return when it finds the first non-trivial factor.
       Uses trial division for num<10e4, Pollard's rho algorithm for num<10e10, quadratic sieve for num<10e100, and general number field sieve for num>10e100
    """
    if num <= 10e4:
        return trial_factors(num, primality_test)
    elif num <= 10e10:
        # TODO Change to rhoFactors
        return trial_factors(num, primality_test)
    elif num <= 10e100:
        # TODO Change to qsFactors
        return trial_factors(num, primality_test)
    else:
        # TODO Change to gnfsFactors
        return trial_factors(num, primality_test)


def trial_factors(num, primality_test=False, include_neg=True):
    """Determines the prime factors of a number by trial division.

       If primalityTest==True (default: False), it will return when it finds the first non-trivial factor.
       If includeNeg==True (default: True), it will include -1 as a factor of negative numbers
    """

    factors_list = []

    # Beyond 2 and 3, any prime number is +/-1 from a multiple of 6, and only
    #   prime numbers need to be checked as factors, so only 6n+/-1 for int n
    #   need to be checked.
    # Only factors up to sqrt(num) need to be tested, because any factor
    #   >sqrt(num) must have a corresponding factor <sqrt(num)
    # Negative numbers are given the factor -1 if includeNeg==True and continue as positive numbers
    # 0, 1, -1 have no factors and returns an empty list

    if num < -1:
        if include_neg:
            factors_list.append(-1)
        num = abs(num)
    elif num <= 1:
        return []

    # Remove all factors that are 2 because 2 is not 6n+/-1
    while num % 2 == 0:
        factors_list.append(2)
        num /= 2
        if primality_test:
            return factors_list

    # Remove all factors that are 3 because 3 is not 6n+/-1
    while num % 3 == 0:
        factors_list.append(3)
        num /= 3
        if primality_test:
            return factors_list

    while num != 1:
        for i in range(6, int(ceil(sqrt(num))) + 6, 6):
            if num % (i - 1) == 0:
                factors_list.append(i - 1)
                if primality_test:
                    return factors_list
                num /= i - 1
                break
            if num % (i + 1) == 0:
                factors_list.append(i + 1)
                if primality_test:
                    return factors_list
                num /= i + 1
                break
        else:
            # neither of the above breaks executed for any prime i+/-1<sqrt(num) so num is prime
            factors_list.append(int(num))
            break

    return factors_list


def is_palindrome(var):
    return str(var) == str(var)[::-1]


def factors_power(num):
    num_factors = factors(num)
    return sorted([(f, num_factors.count(f)) for f in set(num_factors)])


def common_prime_factors(num1, num2):
    common_factors = []
    factors1 = factors_power(num1)
    factors2 = factors_power(num2)
    while len(factors1) > 0 and len(factors2) > 0:
        if factors1[0][0] == factors2[0][0]:
            common_factors.append((factors1[0][0], min(factors1[0][1], factors2[0][1])))
            del factors1[0]
            del factors2[0]
        else:
            if factors1[0][0] < factors2[0][0]:
                del factors1[0]
            else:
                del factors2[0]
    return common_factors


def polygonal_num(poly, n):
    # My attempt at a switch
    return int([-1, -1, -1,                 # 0, 1, and 2 have no polygonal numbers
                lambda a: a*(a+1)/2,        # Triangular numbers
                lambda a: a*a,              # Square Numbers
                lambda a: a*(3*a-1)/2,      # Pentagonal
                lambda a: a*(2*a-1),        # Hexagonal
                lambda a: a*(5*a-3)/2,      # Heptagonal
                lambda a: a*(3*a-2)         # Octagonal
                ][poly](n+1))


def serial_polygonal(poly):
    i=0
    while True:
        yield polygonal_num(poly, i)
        i += 1


def points_on_layer(layer, dim):
    # points on a given layer of a dim-dimensional cube. sum(point_coordinates)==layer for every point on layer
    if dim == 1:
        yield [layer]
    else:
        # points = []
        for z in range(0, layer + 1):
            for point in points_on_layer(layer - z, dim - 1):
                yield ([z] + point)  # points.append([z] + point)
                # return points


def serial_cube(dim):
    i = 0
    while True:
        layer = points_on_layer(i, dim)
        for point in layer:
            yield point
        i += 1


def unique_points_on_layer(layer, dim):
    # Points on a layer that are not rotations of each other
    if dim == 1:
        yield [layer]
    else:
        for z in range(0, int(layer/dim) + 1):
            for point in unique_points_on_layer(layer - z, dim - 1):
                yield ([z] + point)


def serial_cube_uniques(dim):
    i = 0
    while True:
        layer = unique_points_on_layer(i, dim)
        for point in layer:
            yield point
        i += 1


def partition(n):
    # I haven't the faintest clue how this works, but it generates the partitions of num and it does it really fast.
    a = [0 for _ in range(n + 1)]
    k, y = 1, n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]


def serial_primes():
    yield 2
    yield 3

    i = 6
    while True:
        if is_prime(i-1):
            yield i-1
        if is_prime(i+1):
            yield i+1
        i += 6


class PrimeList(list):
    """
        Generates sequential primes, storing them in a list.
        It is most efficient to access in sequential order; \
        if a requested index is larger than the current list, all primes up to that index are generated.

    """
    def __init__(self):
        self.currList = []
        self.primeGen = serial_primes()

    def __next__(self):
        self.currList.append(next(self.primeGen))
        return self.currList[-1]

    def __getitem__(self, key):
        """
        Gets the key'th prime number, either from the list of primes already generated,
        or if key is the length of the list or larger, generates the next prime with next(self)
        and calls itself recursively until the list is key long.

        :param key: The index of the prime to return
        :return: The key'th prime number
        """
        if key >= len(self.currList):
            next(self)
            return self[key]
        else:
            return self.currList[key]

    def __setitem__(self, key, value):
        raise TypeError("PrimeList does not support item assignment; you cannot redefine primes")

    def __delitem__(self, key, value):
        raise TypeError("PrimeList does not support item deletion; you cannot delete primes")
