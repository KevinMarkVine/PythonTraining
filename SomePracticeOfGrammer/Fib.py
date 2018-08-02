#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__,变成私有变量
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    

#    如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
#    该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
#    直到遇到StopIteration错误时退出循环。
    
    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

#取元素getitem,判断元素类型的原因是实现[x:y]的切片输出
    def __getitem__(self,n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
