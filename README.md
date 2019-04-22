# 廖雪峰的Python学习笔记
### **第一章、Python基础：**
#### 数据类型和变量：
    1. 能直接处理的：整数、浮点数、字符串、布尔值、空值
    2. python的整数没有大小限制。浮点数也没有，但是浮点数超过一定范围会表示为inf（无限大），最好用科学计数法表示，例如：1.23*10^9=1.23e9=12.3e8
    3. Python 的整数运算永远是精确的，包括除法，浮点数
    4. 字符串中如果需要’,”这种，用转义字符\，例如：’I\’m   \”ok\”!’就是I’m   ”ok”!
    5. 换行和转义有多种方式，加个r就是不用转义，前提是r放在“前面
    6. 与或非：and，or，not。空值用none表示，不是0
    7. 变量本身类型不固定的语言称为动态语言
    8. 除法分为：正常除法/，和地板除//,地板除的结果是整数部分
#### 字符串和编码：
	1. ASCII码中，A65，z122
	2. acaii码不能表示其他字符，unicode可以，但是unicode定长，容易造成存储空间浪费，才有了变长的UTF-8
	3. ord（）用于获取字符的整数，chr（）把整数表示为编码
    4. len（）计算str的字符数，len（b‘’）计算字节数
    5. 使用内建的isinstance函数可以判断一个变量是不是字符串：
        >>> x = 'abc'
        >>> y = 123
        >>> isinstance(x, str)
        True
        >>> isinstance(y, str)
        False

```
例子：
1.  a = 'ABC'
    b = a
    a = 'XYZ'
    print(b)
结果：ABC

2. 'Hello, %s'   %  'world'
结果：'Hello, world'

3. 'Hi, %s, you have $%d.'   %   ('Michael', 1000000)
结果：'Hi, Michael, you have $1000000.'

4. >>> t = (1)
   >>> t
结果：1

    >>> t = (1,)
    >>> t
结果：(1,)
```
#### 列表和元祖：
    1. List[-2]表示倒数第二个
	2. List.append(‘x’)可以追加元素到末尾，List.insert (位置,内容)，list.pop()删除末尾元素，如果指定删除，括号中加入位置
	3. 列表嵌套就当作二维列表，两个[][]前面写在list中下标，后面写嵌套list中下标
    4. 元祖是括号，一旦初始化就不能修改。如果想要改变，就在元祖内部嵌一个list
#### 字典dict和set：
    1. Python中的dict和C++中的map差不多是一种类型
	2. 通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
		>>> d.get('Thomas')
		>>> d.get('Thomas', -1)
		-1
	3. 要删除一个key，用pop(key)方法
    4. set中重复的元素不会打印出来

### **第二章、函数（有点难）：**
#### 函数参数：
	1. 可以定义空函数pass，让程序先运行起来
    2. python设置默认参数的时候：必须必选参数在前，默认参数在后，降低了函数调用的难度n
	3. 默认参数必须指向不变对象
	4. 可变参数，就是在形参前面加*，*nums表示把nums这个list的所有元素作为可变参数传进去。
	5. 关键字参数很有用，**kw。比如：正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
	6. 限制关键字参数：def person(name, age, *, city, job):
	7. Python定义函数的时候，可以用参数组合，但是顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
	例：
		def f1(a, b, c=0, *args, **kw):
		     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
		
		>>> f1(1, 2)
		a = 1 b = 2 c = 0 args = () kw = {}
		>>> f1(1, 2, c=3)
		a = 1 b = 2 c = 3 args = () kw = {}
		>>> f1(1, 2, 3, 'a', 'b')
		a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
		>>> f1(1, 2, 3, 'a', 'b', x=99)
		a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
		>>> f2(1, 2, d=99, ext=None)
		a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
	7. 递归函数容易栈溢出，可以用尾递归优化
```
例子：
    def add_end(L=[]):
        L.append('END')
        return L
结果：
    >>> add_end()
        ['END']
    >>> add_end()
        ['END', 'END']
    >>> add_end()
        ['END', 'END', 'END']
	
    def add_end(L=None):
        if L is None:
            L = []
        L.append('END')
        return L
结果：
    >>> add_end()
        ['END']
    >>> add_end()
        ['END']
```
### **第三章、高级特性：**
#### 切片：
    1. 切片就是取list或者tuple的部分函数，例如：m[0:3]表示从0开始到3位置，左闭右开
	2. 倒数的第一个元素是-1
	3. 前10个数，每两个取一个：
        >>> L[:10:2]
            [0, 2, 4, 6, 8]
	4. 所有数，每5个取一个：
        >>> L[::5]
        [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
#### 迭代：
	1. 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
	2. 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
	3. 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
	>>> from collections import Iterable
	>>> isinstance('abc', Iterable) # str是否可迭代
	True
#### 列表生成器：
	1. 生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？
	方法一：
	>>> L = []
	>>> for x in range(1, 11):
	...    L.append(x * x)
	...
	>>> L
	[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	
	方法二：
	>>> [x * x for x in range(1, 11)]
	[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	
	2. for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
	>>> [x * x for x in range(1, 11) if x % 2 == 0]
	[4, 16, 36, 64, 100]
	
	3. 还可以使用两层循环，可以生成全排列：
	>>> [m + n for m in 'ABC' for n in 'XYZ']
    ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
#### 生成器（generator）：

	1. 生成器的意义：不知道访问的元素，如果贸然创建很大的列表，会造成巨大的空间浪费，因此，我们尝试在循环的过程中不断推算出后续的元素，这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器
	2. 因此，generator中保存的是算法
	3. 定义generator的两种方法：
		a. 只要把一个列表生成式的[]改成()，就创建了一个generator：
		>>> L = [x * x for x in range(10)]
		>>> L
		[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
		>>> g = (x * x for x in range(10))
		>>> g
		b. 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
	4. 函数和generator的区别：函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
	5. 用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
	
#### 迭代器：
	1. 所有能够用于for循环的对象：list、tuple、set、str、generator等都叫作可迭代对象，可以用isinstance判断一个对象是否是可迭代对象
	2. 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
	3. isinstance可以判断对象是可迭代对象还是迭代器对象，取决于第二个参数，如：
	可以使用isinstance()判断一个对象是否是Iterable对象：
	>>> isinstance('abc', Iterable)
	True
	可以使用isinstance()判断一个对象是否是Iterator对象：
	>>> isinstance('abc', Iterator)
	False
	4. 迭代器对象和可迭代对象的区别：能否被next（）函数调用并不断返回下一个值。可用iter（）转换
	5. 为什么list、dict、str等数据类型不是Iterator？简单来说，因为他们不够大

### **第四章、函数式编程：**
	函数式编程是一种抽象程度很高的编程范式，允许把函数本身作为参数传入另一个参数，还允许返回一个函数

#### 高阶函数：
	1. 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式
	2. 变量可以指向函数，指向函数之后，这个变量就可以实现函数功能
	3. 也可以把函数名看作是变量
#### Map/reduce:
	1. map作为高阶函数，把运算规则抽象了。
	Eg.  把这个list所有数字转为字符串：
	>>> list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
	['1', '2', '3', '4', '5', '6', '7', '8', '9']
	
	2. Reduce()是作用在一个序列之上。
	Eg.  对一个序列求和，就可以用reduce实现：
	>>> from functools import reduce
	>>> def add(x, y):
	...     return x + y
	...
	>>> reduce(add, [1, 3, 5, 7, 9])
	25


