##__slots__
前言：了解他的用法先了解一下知识点：
- 给实例添加属性与方法的方法
- 给类添加属性方法的方法
- 以上两者的区别，继承时有什么特点

###给实例添加属性与方法
- 给实例添加属性
```
class Student(object):
    pass
然后，尝试给实例绑定一个属性：
>>> s = Student()
>>> s.name = 'Michael' # 动态给实例绑定一个属性
>>> print(s.name)
Michael
```
- 给实例添加方法（非给类添加方法）  使用MethodType添加
```
>>> def set_age(self, age): # 定义一个函数作为实例方法
...     self.age = age
...
>>> from types import MethodType
>>> s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
>>> s.set_age(25) # 调用实例方法
>>> s.age # 测试结果
25
```
- 给实例绑定的方法对其他实例不起作用
此处不再赘述

###给类添加属性与方法
- 给类绑定属性
```
可以在绑定类方法时同时绑定属性
```

- 给类绑定方法
动态创建过程中，给类绑定方法，则所有的实例化对象均可以访问
```
>>> def set_score(self, score):
...     self.score = score
...
#此处必须要用类调用绑定，负否则后续无法使用实例赋值
>>> Student.set_score = set_score

#测试
#调用类方法
>>> s.set_score(100)
#调用类属性
>>> s.score
100
>>> s2.set_score(99)
>>> s2.score
99

```
通常情况下，上面的set_score方法可以直接定义在class中，但动
态绑定允许我们在程序运行的过程中动态给class加上功能，这在静
态语言中很难实现。


###.__slots__的使用
目的：限制实例的属性
方法：为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，
来限制该class实例能添加的属性
```
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
```

```
测试
```
>>> s = Student() # 创建新的实例
>>> s.name = 'Michael' # 绑定属性'name'
>>> s.age = 25 # 绑定属性'age'
>>> s.score = 99 # 绑定属性'score'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'score'
由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。

注意：使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
```

###总结
- 1.python支持动态给类和实例增加属性和方法；
- 2.python __slots__只能限制实例的属性及方法，对于类则没有影响，对于子类则更是没有限制。
- 3.将方法绑定给类后，类调用方法后，类和实例都可以访问类中的属性与方法，这不受__slots__范围限制
- 4.方法没有绑定给类而直接绑定给实例时，需要在__slots__规定范围中加入该方法和方法中的属性
