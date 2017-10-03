# https://projecteuler.net/problem=56

maxSum = 0
for a in range(0, 100):
    for b in range(0, 100):
            # Convert pow(a,b) to a string, create a list of the int conversion of each character and sum it
        digitSum = sum([int(c) for c in str(pow(a,b))])
        maxSum = digitSum if digitSum > maxSum else maxSum

print(maxSum)
