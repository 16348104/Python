# coding=utf-8
def people(age):
    if age > 0:
        print("正常")
        name = get_name()
    else:
        print('不正常!')


def get_name():
    return 'abc'

people(10)
