# __author__ = 'zb'
def main():
    fname = eval(input("输入文件名:"))
    infile = open(fname, "r")
    data = infile.read()
    print(data)

main()