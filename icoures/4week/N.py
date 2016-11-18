# __author__ = 'zb'
def main():
    n = eval(input("How many nunmbers are there?"))
    max = eval(input("Enter a number."))
    for i in range(n - 1):
        x = eval(input("Enter a number."))
    if x > max:
        max = x
    print("最大的是", max)


main()