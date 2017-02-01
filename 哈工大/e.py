# import math
#
# e = 1
# for i in range(1, 100):
#     e += 1.0 / math.factorial(i)
# print 'e is:', e

e = 1
factorial = 1
for i in range(1, 100):
    factorial *= i
    e += 1.0 / factorial
print 'e is:', e
