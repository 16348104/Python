# __author__ = 'zb'
def main():
    PM = eval(input("what is today's PM2.5?"))
    if PM < 35:
        print("Good. Go runing")
    elif PM < 75:
        print("Moderate.Go walking")
    elif PM < 115:
        print("Unhealthy for sensitive group!")
    elif PM < 150:
        print("Unhealthy.Limit prolonged exertion!")
    elif PM < 250:
        print("Very unhealthy.Avoid prolonged exertion")
    else:
        print("Hazardous.REMAIN INDOORS!")

main()

