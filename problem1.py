# https://projecteuler.net/problem=1

sum = 0
# add all multiples of 3 to sum
for i in range(0, 1000, 3):
    sum += i
# add all multiples of 5 to sum, if they're not a multiple of 3. (so 15, 30, 45, etc. aren't duplicated)
for i in range(0, 1000, 5):
    if i%3 != 0:
        sum += i
print(sum)
