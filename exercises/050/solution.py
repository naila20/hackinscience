sum = 0
for i in range(1, 1000):
    if 5*i < 1000:
        sum = sum + 5*i
    if 3*i < 1000:
        sum = sum + 3*i
for n in range(1, 66):
    sum = sum - 3*5*n
print(sum)
