'''__author__ = 'zb'


'''


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

n = int(raw_input('input a number:'))
print n,">>>",fib(n)
