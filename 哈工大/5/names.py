# __author__ = 'dell'
import re

f = open('names.txt', 'r')


def is_panlindrom(name):
    low = 0
    hight = len(name) - 1
    while low < hight:
        if name[low] != name[hight]:
            return False

        low += 1
        hight -= 1
    return True


def is_panlindrom_rec(name):
    if len(name) < 2:
        return True
    if name[0] == name[-1]:
        return is_panlindrom_rec(name[1:-1])
    else:
        return False


def is_ascending(name):
    p = name[0]
    for c in name:
        if p < c:
            return False
        p == c
    return True

# regular expressions
for line in f:
    pattern = 'C.A'
    result = re.search(pattern, line)
    line = line.strip()
    # if is_panlindrom_rec(line):
    # if is_panlindrom(L):
    # if is_ascending(line):
    if result:
        print 'name is {}'.format(line)
f.close()
