# __author__ = 'zb'
num = 151


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def is_palin(num):
    num_t = num
    num_p = 0

    while num_t != 0:
        num_p = num_p * 10 + num_t % 10
        num_t = num_t / 10

    if num == num_p:
        return True
    else:
        return False


if is_prime(num) and is_palin(num):
    print 'YES'
else:
    print 'NO'
