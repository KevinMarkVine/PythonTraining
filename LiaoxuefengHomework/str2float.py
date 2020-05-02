# coding: UTF-8
'''
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
'''
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}


def str2float(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    
    a = list(map(char2num, s))
    b = len(a)
    c = a.index('.')
    print(a)
    a.remove('.')
    
    return (reduce(fn, a))/(10**(b - c - 1))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
    
    
    
    
# def str2float(s):
#     def fn(x, y):
#         return x * 10 + y
#     def char2num(s):
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#     # 得到字符串中.的索引
#     n = s.index('.')
#     # 根据.的位置将字符串切片为两段
#     s1 = list(map(int, [x for x in s[: n]]))
#     s2 = list(map(int, [x for x in s[n + 1 :]]))
#     # m ** n表示m的n次方
#     return reduce(fn, s1) + reduce(fn, s2) / 10 ** len(s2)
