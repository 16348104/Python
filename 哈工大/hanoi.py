# __author__ = 'zb'
count = 0


def hanoi(n, A, B, C):
    global count
    if n == 1:
        print 'Move disk', n, 'from', A, 'to', C
        count += 1
    else:
        hanoi(n - 1, A, B, C)
        print 'Move disk', n, 'from', A, 'to', C
        count += 1
        hanoi(n - 1, B, A, C)


hanoi(7, 'left', 'mid', 'right')
print count

# 2**n-1