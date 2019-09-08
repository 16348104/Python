str1 = eval(input('请输入一个数字:'))
# 非0数值，非空数据类型等价于True
# 0等价于False,可以直接又作判断条件
print('输入的数是', str1)
if str1 % 2:
    print('这是个奇数！')
else:
    print("这是个偶数！")
