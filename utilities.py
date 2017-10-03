##
## Contains functions for basic math operations that will be reused
##

from math import *

def isPrime(num, negativePrime=True):
    """Determines is a number is prime

       If negativePrime==True (default: True), then negative numbers can be prime
    """
    if negativePrime:
        num = abs(num)

    a = factors(num, True)
    return a != [] and a[0] == num

def factors(num, primalityTest=False):
    """Determines the prime factors of a number

       If primalityTest==True (default: False), it will return when it finds the first non-trivial factor.
       Uses trial division for num<10e4, Pollard's rho algorithm for num<10e10, quadratic sieve for num<10e100, and general number field sieve for num>10e100
    """
    if num <= 10e4:
        return trialFactors(num, primalityTest)
    elif num <= 10e10:
        #TODO Change to rhoFactors
        return trialFactors(num, primalityTest)
    elif num <= 10e100:
        #TODO Change to qsFactors
        return trialFactors(num, primalityTest)
    else:
        #TODO Change to gnfsFactors
        return trialFactors(num, primalityTest)

def trialFactors(num, primalityTest=False, includeNeg=True):
    """Determines the prime factors of a number by trial division.

       If primalityTest==True (default: False), it will return when it finds the first non-trivial factor.
       If includeNeg==True (default: True), it will include -1 as a factor of negative numbers
    """

    factors = []
    originalNum = num

    # Beyond 2 and 3, any prime number is +/-1 from a multiple of 6, and only
    #   prime numbers need to be checked as factors, so only 6n+/-1 for int n
    #   need to be checked.
    # Only factors up to sqrt(num) need to be tested, because any factor
    #   >sqrt(num) must have a corresponding factor <sqrt(num)
    # Negative numbers are given the factor -1 if includeNeg==True and continue as positive numbers
    # 0, 1, -1 have no factors and returns an empty list

    if num < -1:
        if includeNeg:
            factors.append(-1)
        num = abs(num)
    elif num <= 1:
        return []

    # Remove all factors that are 2 because 2 is not 6n+/-1
    while num%2==0:
        factors.append(2)
        num /= 2
        if primalityTest:
            return factors

    # Remove all factors that are 3 because 3 is not 6n+/-1
    while num%3==0:
        factors.append(3)
        num /= 3
        if primalityTest:
            return factors

    while num != 1:
        for i in range(6, int(ceil(sqrt(num)))+6, 6):
            if num % (i-1) == 0:
                factors.append(i-1)
                if primalityTest:
                    return factors
                num /= i-1
                break
            if num % (i+1) == 0:
                factors.append(i+1)
                if primalityTest:
                    return factors
                num /= i+1
                break
        else:
            # neither of the above breaks executed for any prime i+/-1<sqrt(num) so num is prime
            factors.append(int(num))
            break

    return factors

def rhoFactors(num, primalityTest=False):
    #TODO
    pass

def qsFactors(num, primalityTest=False):
    #TODO
    pass

def gnfsFactors(num, primalityTest=False):
    #TODO
    pass

def isPalindrome(var):
    return str(var) == str(var)[::-1]

def factorsPower(num):
    numFactors = factors(num)
    return sorted([(f, numFactors.count(f)) for f in set(numFactors)])

def commonPrimeFactors(num1, num2):
    commonFactors = []
    factors1 = factorsPower(num1)
    factors2 = factorsPower(num2)
    while len(factors1) > 0 and len(factors2) > 0:
        if factors1[0][0] == factors2[0][0]:
            commonFactors.append((factors1[0][0], min(factors1[0][1], factors2[0][1])))
            del factors1[0]
            del factors2[0]
        else:
            if factors1[0][0] < factors2[0][0]:
                del factors1[0]
            else:
                del factors2[0]
    return commonFactors
