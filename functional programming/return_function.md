##返回函数
####概念
```
把函数作为结果值返回
```

####代码解析
```
定义一个常规的可变参数的函数，代码如下：
def test_sum():
    init=0
    for n in args:
        init+=n
    return init

作为对比，然后定义一个返回函数的函数：
def call_sum(*args):
    def test_sum():
        init=0
        for n in args:
            init+=n
        return init
    return test_sum

第一个常规函数进行测试如下：
print(test_sum(1,2,3,4))    #10

第二个函数测试：
print(call_sum(1,2,3,4))    
#则结果为赋值函数，为<function call_sum.<locals>.test_sum at 0x000001AA998F4510>
#返回的是求和函数而非结果

当要得到结果则，可以在函数后面加一对括号，如下：
print(call_sum(1,2,3,4)())     #10


另外常见的一种理解如下：
f=call_sum(1,2,3,4)
print(f)           #返回函数，<function call_sum.<locals>.test_sum at 0x000001AA998F4510>
print(f())         #返回结果，为10

```

####其他引深点
```
f1=call_sum(1,2,3,4)
f2=call_sum(1,2,3,4)
print(f1)            #<function call_sum.<locals>.test_sum at 0x000001A493D54510>
print(f2)            #<function call_sum.<locals>.test_sum at 0x000001A493FDA620>
print(f1==f2)        #False


可以看出每次返回一个新的函数，另外f1与f2调用互不影响
在返回函数的基础上引出闭包的感念，详细请看detail_closure文件
```



####应用场景
```

```
