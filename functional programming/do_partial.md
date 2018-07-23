##Partial function
####概念
```
通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点，
由functools模块提供功能
int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换
作用：降低函数调用的难度

```

####代码解析
```
import functools
int2=functools.partial(int,base=8)
print(int2('11'))
#9
按八进制转换则得到数值为9

print(int2('111'))
#73

注意：是将指定的原始数据，按照指定的base进制进行转换

```
####应用场景
- 1.实现一个偏函数
```
class partial:
    def __new__(cls, func, *args, **kwargs):
        if not callable(func):
            raise TypeError("the first argument must be callable")
        self = super().__new__(cls)

        self.func = func
        self.args = args
        self.kwargs = kwargs
        return self

    def __call__(self, *args, **kwargs):
        newkeywords = self.kwargs.copy()
        newkeywords.update(kwargs)
        return self.func(*self.args, *args, **newkeywords)

    #以下写法，无法支持覆盖，上面的写法未优化后的写法
    #def __call__(self, *args, **kwargs):
        #return self.func(*self.args, *args, **self.kwargs, **kwargs)
```





####其他
