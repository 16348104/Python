import math

def main():
    print("The program find the real solutions to quadratic\n ")
    a, b, c = eval(input("Please enter the coefficients (a,b,c):"))
    delta = b * b - 4 * a * c
    if delta < 0:
        print("\nThe equation has no real roots ")
    else:
        delta = math.sqrt(delta)
        r1 = (-b + delta) / (2 * a)
        r2 = (-b - delta) / (2 * a)
        print("\nThe solutions are:", r1, r2)

main()



