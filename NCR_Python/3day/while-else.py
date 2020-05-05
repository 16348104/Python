# n=0
# while n<10:
#     print(n)
#     n+=3
# print("程序结束!")
# while和else,while语句正常执行后执行else语句


s, num = 'py', 0
while num < len(s):
    print("程序执行中：" + s[num])
    num += 1
else:
    s = '程序结束!'
print(s)
