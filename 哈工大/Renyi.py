# __author__ = 'zb'
# renyi

import random


def park(low, hight):
    if hight - low < 1:
        return 0
    else:
        x = random.uniform(low, hight - 1)
        return park(low, x) + park(x + 1, hight) + 1


sum = 0
for i in range(1, 1000):
    sum += park(0, 5)
print sum / 1000.0


