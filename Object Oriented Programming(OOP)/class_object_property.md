##实例属性和类属性
- 1.什么叫示例属性
- 2.什么叫类属性
- 3.两者之间的区别关系



###概念
- 实例属性
```
由于Python是动态语言，根据类创建的实例可以任意绑定属性。
给实例绑定属性的方法是：
通过实例变量，
或者通过self变量：

示例：
#通过self
class Student(object):
    def __init__(self, name):
        self.name = name

#通过示例变量
s = Student('Bob')
s.score = 90

```

- 类属性
```
如果Student类本身需要绑定一个属性呢，可以直接在class中定义属性，
这种属性是类属性，归Student类所有

示例：
class Student(object):
    name = 'Student'

定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到
```

###代码解析
```
>>> class Student(object):
...     name = 'Student'
...
>>> s = Student() # 创建实例s
>>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
Student
>>> print(Student.name) # 打印类的name属性
Student
>>> s.name = 'Michael' # 给实例绑定name属性
>>> print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
Michael
>>> print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
Student
>>> del s.name # 如果删除实例的name属性
>>> print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
Student

注意：在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，
因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用
相同的名称，访问到的将是类属性
```

###应用场景
- 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
```
class Person(object):
    count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.count+=1

#注意：这里使用Person.count而不是self.count,在创建实例时会启动__init__函数，
进而可以实现类的增加，而使用self.count,是指实例对象的属性

print(Person.count)      #0
a=Person('liuhu',24)
a.count=0
print(a.count)           #0
print(Person.count)      #1
b=Person('liuli',28)
print(a.count)          #0
print(Person.count)     #2

```

###总结
- 实例属性属于各个实例所有，互不干扰；
- 类属性属于类所有，所有实例共享一个属性；
- 不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
