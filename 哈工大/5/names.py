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


for line in f:
    line = line.strip()
    if is_panlindrom(line):
        print line
f.close()
