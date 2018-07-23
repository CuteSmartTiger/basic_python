##获取对象信息
作用：知道对象的类型  属性  方法等信息，方便操作使用


###相关使用方法
####type()
- 判断类型
```
>>> type(123)
<class 'int'>
>>> type('str')
<class 'str'>
>>> type(None)
<type(None) 'NoneType'>
```

- 可以了解变量指向的函数或者类型
```
>>> type(abs)
<class 'builtin_function_or_method'>

#a为之前定义类的示例对象
>>> type(a)
<class '__main__.Animal'>
```


- 判断对象是否是函数：使用types模块中定义的常量：
```
>>> import types
#自己定义函数
>>> def fn():
...     pass
...
#使用FunctionType判断是否是函数
>>> type(fn)==types.FunctionType
True
#使用BuiltinFunctionType判断是否是内建函数
>>> type(abs)==types.BuiltinFunctionType
True
>>> type(lambda x: x)==types.LambdaType
True
>>> type((x for x in range(10)))==types.GeneratorType
True
```
####isinstance()
- 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数
```
并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
>>> isinstance([1, 2, 3], (list, tuple))
True
>>> isinstance((1, 2, 3), (list, tuple))
True
```

总之：总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

#### dir()
- 概念
```
要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
```

- 示例
```
>>> dir('ABC')
['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']
```

- 特殊方法
```
类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，
如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的
__len__()方法，所以，下面的代码是等价的：

>>> len('ABC')
3
>>> 'ABC'.__len__()
3
```
- 普通方法
```
剩下的都是普通属性或方法，比如lower()返回小写的字符串：

>>> 'ABC'.lower()
'abc'

而不能写成lower('ABC')
```
<!-- 注意：如何判断两者，两者的区别，调用方法 -->

####getattr()、setattr()、hasattr()
目的：直接操作一个对象的状态

- 定义一个类并实例化对象
```
>>> class MyObject(object):
...     def __init__(self):
...         self.x = 9
...     def power(self):
...         return self.x * self.x
...
>>> obj = MyObject()
```
- 紧接着，可以测试该对象的属性：
```
>>> hasattr(obj, 'x') # 有属性'x'吗？
True
>>> obj.x
9
>>> hasattr(obj, 'y') # 有属性'y'吗？
False
>>> setattr(obj, 'y', 19) # 设置一个属性'y'
>>> hasattr(obj, 'y') # 有属性'y'吗？
True
>>> getattr(obj, 'y') # 获取属性'y'
19
>>> obj.y # 获取属性'y'
19
```
注意：通过以上操作，我可以了解到想，x  y属于属性，def 中的power等为方法


```
如果试图获取不存在的属性，会抛出AttributeError的错误：
>>> getattr(obj, 'z') # 获取属性'z'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'MyObject' object has no attribute 'z'

可以传入一个default参数，如果属性不存在，就返回默认值：
>>> getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
404
```
- 也可以获得对象的方法：
```
>>> hasattr(obj, 'power') # 有属性'power'吗？
True
>>> getattr(obj, 'power') # 获取属性'power'
<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
>>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
>>> fn # fn指向obj.power
<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
>>> fn() # 调用fn()与调用obj.power()是一样的
81
```
