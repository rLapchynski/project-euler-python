# https://projecteuler.net/problem=57

num, den, i = 1, 2, 0
for _ in range(0, 1000):
    num, den = den, num+2*den
    i += 1 if len(str(num+den)) > len(str(den)) else 0

print(i)
