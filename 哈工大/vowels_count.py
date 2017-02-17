# __author__ = 'zb'

def vowels_count(string):
    ret = 0
    for char in string:
        # print char
         if char in 'aeiouAEIOU':
           ret = ret + 1
    return ret

print vowels_count('zhanghuanxin')

