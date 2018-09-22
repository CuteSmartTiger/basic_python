 ##callable()函数


####概念
```
callable() 函数用于检查一个对象是否是可调用的。如果返回True，object仍然可能调用失败；
但如果返回False，调用对象ojbect绝对不会成功。
对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True。
```

####实例
```
>>>callable(0)
False
>>> callable("runoob")
False

>>> def add(a, b):
...     return a + b
...
>>> callable(add)             # 函数返回 True
True
>>> class A:                  # 类
...     def method(self):
...             return 0
...
>>> callable(A)               # 类返回 True
True
>>> a = A()
>>> callable(a)               # 没有实现 __call__, 返回 False
False
>>> class B:
...     def __call__(self):
...             return 0
...
>>> callable(B)
True
>>> b = B()
>>> callable(b)               # 实现 __call__, 返回 True
True

注：类在实例化时如果需要可以调用，则需要定义__call__方法
```

####其他
