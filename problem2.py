# https://projecteuler.net/problem=2

num = 0
prevNum1 = 0
prevNum2 = 1
sum = 0

while num < 4000000:
    num = prevNum1 + prevNum2
    prevNum1 = prevNum2
    prevNum2 = num

    if num%2 == 0:
        sum += num
        
print(sum)
