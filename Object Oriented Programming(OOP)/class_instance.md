##class
####类的定义
面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的
模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象
都拥有相同的方法，但各自的数据可能不同


####代码解析
- 面向过程与面向对象的区别
```
面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。

而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。
```
- 类与实例的关系
```
class Student(object):
    pass


>>> bart = Student()
>>> bart
<__main__.Student object at 0x10a67a590>

>>> Student
<class '__main__.Student'>

由以上可见，Student是类，而bart则是实例，是由类创建的对象，
同时可知类创建实例的方法为：类名+（）


补充说明：类（Class）和实例（Instance）的概念是很自然的。Class是一种抽象概念，
比如我们定义的Class——Student，是指学生这个概念，而实例（Instance）
则是一个个具体的Student
```

- 给类定义属性与方法
```
class Student(object):
    #通过init初始相关属性
    def __init__(self, name, score):
        self.name = name
        self.score = score
    #定义这个类的方法
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

总结：一个类，可以由属性与方法组成，对象与对象之间通过方法沟通
```

- 给对象发消息
```
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

给对象发消息实际上就是调用对象对应的关联函数，我们称之为对象的方法（Method）
```

- 创建类时继承object与不继承的区别
```
在python3.x中可以两者没有差别
在python2系列中，有明显的区别，即继承object的会继承object类下的属性与方法
```

####小结
- 类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
- 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
- 通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
- 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然
它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
