# https://projecteuler.net/problem=57

num, den, = 1, 2

for _ in range(0, 5):
    num += 2*den
    num, den = den, num
    num += den
    print(num, den)
