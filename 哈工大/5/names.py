# __author__ = 'dell'

f = open('names.txt', 'r')
for line in f:
    line = line.strip()
    print line.title()
f.close()
