sum = 0
x = 1
while True:
    if x % 2 == 0:
        continue
    sum = sum + x
    x = x + 2
    if x > 100:
        break
print sum
