# eval(字符串)函数能够以python表达式的方式解析并执行字符串，将返回结果输出
# utf-8

a = eval(input("请输入数字："))
b = type(a)
print('a的值{},a的类型{}'.format(a, b))

