# __author__ = 'dell'

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
    if name[0]==name[-1]:
        return is_panlindrom_rec(name[1:-1])
    else:
        return False


for line in f:
    line = line.strip()
    if is_panlindrom_rec(line):
        # if is_panlindrom(L):
        print line
f.close()
