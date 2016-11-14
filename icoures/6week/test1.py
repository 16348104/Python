# __author__ = 'zb'
def main():
    fname = eval(input("Enter filename:"))
    infile = open(fname, "r")
    data = infile.read()
    print(data)


main()