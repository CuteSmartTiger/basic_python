##多重继承（Multiple Inheritance）
目的：继承是面向对象编程的一个重要的方式，因为通过继承，子类就可以扩展父类的功能。


###super的使用
目的：父类多次被调用时只执行一次， 优化了执行逻辑

####代码示例
- 不使用super()函数
```
class A:
  def __init__(self):
    print("Enter A")
    print("Leave A")
class B(A):
  def __init__(self):
    print("Enter B")
    A.__init__(self)
    print("Leave B")
class C(A):
  def __init__(self):
    print("Enter C")
    A.__init__(self)
    print("Leave C")
class D(A):
  def __init__(self):
    print("Enter D")
    A.__init__(self)
    print("Leave D")
class E(B, C, D):
  def __init__(self):
    print("Enter E")
    B.__init__(self)
    C.__init__(self)
    D.__init__(self)
    print("Leave E")


>>>E()
结果：
Enter E
Enter B
Enter A
Leave A
Leave B
Enter C
Enter A
Leave A
Leave C
Enter D
Enter A
Leave A
Leave D
Leave E

可见公共A类被调用很多次
```

- 使用super()函数
```
class A:
  def __init__(self):
    print("Enter A")
    print("Leave A")
class B(A):
  def __init__(self):
    print("Enter B")
    super(B, self).__init__()
    print("Leave B")
class C(A):
  def __init__(self):
    print("Enter C")
    super(C, self).__init__()
    print("Leave C")
class D(A):
  def __init__(self):
    print("Enter D")
    super(D, self).__init__()
    print("Leave D")
class E(B, C, D):
  def __init__(self):
    print("Enter E")
    super(E, self).__init__()
    print("Leave E")

>>>E()

#结果：
Enter E
Enter B
Enter C
Enter D
Enter A
Leave A
Leave D
Leave C
Leave B
Leave E

可见公共类A只被执行了一次，至于执行的顺序，是按照
MRO（Method Resolution Order）方法解析顺序进行的
```
