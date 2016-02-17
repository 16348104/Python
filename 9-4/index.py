d = {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74}
sum = 0.0
for k, v in d.items():
    sum = sum + v
    print k, ':', v
print 'average', ':', sum / len(d)
