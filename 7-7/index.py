def average(*args):
    sum = 0.0
    if len(args) == 0:
        return sum
    for x in args:
        sum = sum + x
    return sum / len(args)

print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)