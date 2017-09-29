sum = 0
for i in range(0, 1000, 3):
    sum += i
for i in range(0, 1000, 5):
    if i%3 != 0:
        sum += i
print(sum)
