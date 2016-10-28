
def main():
    pm = eval(input("what is today's PM2.5?"))
    if pm > 75:
        print("Unhealthy.Be careful!")
    if pm < 35:
        print("Good.Go runing!")
main()