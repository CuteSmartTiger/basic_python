##customize class
 ```
用途：可以按照自己的需求定制类
定制类需要注意__XX__形式上的变量或者函数名
 ```

###__str__()方法：返回一个好看的字符串

 ```
 >>> class Student(object):
         def __init__(self, name):
             self.name = name
        def __str__(self):
             return 'Student object (name: %s)' % self.name

>>> print(Student('Michael'))
Student object (name: Michael)
 ```

###__repr__()方法
__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
```
>>> class Student(object):
      def __init__(self, name):
          self.name = name
      def __str__(self):
          return 'Student object (name=%s)' % self.name
      __repr__ = __str__


>>> s=Student('liuhu')
>>> s
Student object (name=liuhu)
>>>
 ```

###__iter__()方法
- 目的：一个类想被用于for ... in循环，类似list或tuple那样
- 方法：实现一个__iter__()方法，该方法返回一个迭代对象，然后，
  Python的for循环就会不断调用该迭代对象的__next__()方法拿到
  循环的下一个值，直到遇到StopIteration错误时退出循环
示例
```
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

#测试
>>> for n in Fib():
...     print(n)
...
1
1
2
3
5
...

```
###__getitem__()方法
- 原因：要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
```
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


>>> f = Fib()
>>> f[0]
1
>>> f[1]
1
>>> f[2]
2
>>> f[3]
3
>>> f[10]
89
>>> f[100]
```


### __call__(): 用于实例自身的调用，达到()调用的效果
可以把此类的对象当作函数来使用，相当于重载了括号运算符
```
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

<!-- 调用 -->
>>> s = Student('Michael')
>>> s() # self参数不要传入
My name is Michael.
```

通过callable()函数，我们就可以判断一个对象是否是“可调用”对象
比如：
```
>>> callable(Student())
True
>>> callable(max)
True
>>> callable([1, 2, 3])
False
>>> callable(None)
False
>>> callable('str')
False
```

### __getattr__(): 当调用不存在的属性时调用此方法来尝试获得属性
- 示例
```
class Chain(object):
    def __init__(self, path=''):    # 默认路径参数path为空
        self._path = path

    def __getattr__(self, path):
        print('call __getattr__(%s)' % path)
        return Chain('%s/%s'% (self._path, path))

    def __str__(self):
        return self._path

    def __call__(self, param):
        print('cal __call__(%s)' % param)
        return Chain('%s/%s' % (self._path, param))

    __repr__ = __str__


<!-- 以下为分析 -->
# /status/user/timeline/list
# Chain().status.user.timeline.list调用分析
# 首先执行Chain()返回一个实例对象C1(path = '')，
# 通过实例对象C1来获取status属性，因为C1中不存在status属性，所以就会调用
# __getattr__()来尝试获取status属性，接着通过__getattr__()方法返回
# 带参数status的实例对象C2(path = '/status')，然后通过实例对象C2来获取user属性，
# C2中不存在user属性，接着调用__getattr__()方法返回带参数user
# 的实例对象C3(path = '/status/user')，然后通过实例对象C3来获取timeline属性，
# 因C3不存在timeline属性，故调用__getattr__()方法返回带参数timeline
# 的实例对象C4(path = '/status/user/timeline')，通过实例对象C4来获取list属性，
# 又因C4中不存在list属性，调用__getattr__()方法返回带参数list
# 的实例对象C5(path = '/status/user/timeline/list')，
# 最后通过调用__str__()方法来打印实例对象C5，即返回/status/user/timeline/list
# 具体参考见下面的测试结果
print(Chain().status.user.timeline.list)
```

- 示例2
```
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99

当调用不存在的属性时，比如score，Python解释器会试图调用
__getattr__(self, 'score')来尝试获得属性，这样，我们就
有机会返回score的值：

>>> s = Student()
>>> s.name
'Michael'
>>> s.score
99
```
