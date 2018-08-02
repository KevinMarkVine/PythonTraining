#1.一个类，要有：构造函数、检查函数值、重设函数值、
#2.用isinstance（a，b）判断a是不是b类型
#3.用type（a）来判断a的类型
#  例如type（132）
#

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        else:
            return 'C'

#判断一个对象是否是函数
import types
def fn():
    pass

#使用
type(fn) == types.FunctionType
type(abs) == types.BuiltinFunctionType
type(lambda x: x) == types.LambdaType


#操作对象属性的方法：getattr()、setattr()、hasattr()


#限制实例的属性用slots、但是这个只对当前类起作用，不继承
class Student(object):
    __slots__ = ('name', 'age') #即，实例只能绑定name和age属性


#@property，可以使用一个函数名执行不同的操作，重载？

