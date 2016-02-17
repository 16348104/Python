d = {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74}
sum = 0.0
for v in d.itervalues():
    sum = sum + v
print sum / len(d)
