# pi = 3.14
# radius = float(raw_input('Radius: '))
# area = pi * radius ** 2
# print 'The area of the circle is: ', area



pi = 0
sign = 1
divisor = 1
for i in range(1, 100000):
    pi += 4.0 * sign / divisor
    divisor += 2
    sign *= -1
print 'pi is:', pi
