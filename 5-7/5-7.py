L = [75, 98, 59, 81, 66, 43, 69, 85]
sum = 0.0
n = 0
for x in L:
    if x < 60:
        continue
    sum = sum + x
    n = n + 1
print sum / n
