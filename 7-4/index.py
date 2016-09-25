import math


def quadratic_equation(a, b, c):
    t = math.sqrt(b * b - 4 * a * c)
    return (-b + t) / (2 * a), (-b - t) / (2 * a)


print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)
