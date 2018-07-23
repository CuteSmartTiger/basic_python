##闭包（closure）

####概念
```
注意到返回的函数在其定义内部引用了局部变量args，所以，
当一个函数call_sum返回了一个函数test_sum后，其内部的
局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
```
####代码解析
```
返回的函数并没有立刻执行，而是直到调用了分f()才执行,了解闭包的运行机理，先看如下代码：
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()

print(f1)    #9
print(f2)    #9
print(f3)    #9

全部都是9,原因就在于返回的f函数引用了变量i，但它并非立刻执行。
等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
如何避免这种情况了

解决方案：方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def colusre_count():
    #def f(j):函数内部实现的是返回函数，通过参数进行绑定
    def f(j):
        def g():
            return j*j
        #返回函数
        return g

    fs = []
    for i in range(1, 4):
        #由于参数通过j绑定，则此处f(1),f(2),f(3)，暂存对应的函数
        fs.append(f(i))             # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1,f2,f3=colusre_count()

```
- 注意点： 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

####其他引申
```


```
####使用场景或示例
```
1.使用生成器，返回递增整数数列生成器
def f():
    def f1():
        n=1
        while True:
            yield n
            n=n+1
    it = f1()
    def f2():
        return next(it)
    return f2

c=f()
print(c(),c(),c())

2.global，适用于函数内部修改全局变量
n=0
def f():
    def f2():
        global n
        n=n+1
        return n
    return f2
c=f()
print(c(),c(),c())


3.nonlocal，适用于嵌套内部函数修改外部函数局部变量
def f():
    n=0
    def f2():
        nonlocal n
        n=n+1
        return n
    return f2
c=f()
print(c(),c(),c())


4.容器法，将变量设置为一个容器，通过下标来修改
#此点有待深入理解
def f():
    s=[0]
    def f1():
        s[0]=s[0]+1
        return s[0]
    return f1
c=f()
print(c(),c(),c())>>>1,2,3

```
