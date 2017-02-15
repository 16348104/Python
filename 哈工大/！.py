# __author__ = 'zb'
'''
def p(n):
    x = 1
    i = 1
    while i <= n:
        x *= i
        i += 1
    return x


n = int(raw_input("input:"))
print n, "p(!):", p(n)
'''



def p(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * p(n - 1)

n = int(raw_input("input:"))
print n, "p(!):", p(n)