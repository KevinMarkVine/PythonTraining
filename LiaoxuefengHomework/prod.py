# coding: UTF-8
'''
编写一个prod()函数，可以接受一个list并利用reduce()求积：
'''
from functools import reduce

def prod(L):
    def chengji(x, y):
        return x * y
    return reduce(chengji, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')