print [m + n for m in 'ABC' for n in '123']

print [100 * x + 10 * y + z for x in range(1, 10) for y in range(10) for z in range(10) if x == z]

L = []
for x in range(1, 10):
    for y in range(10):
        for z in range(1, 10):
            if x == z:
                L.append(100 * x + 10 * y + z)
print L
