##property
- 为什么使用property
```
@property广泛应用在类的定义中，可以让调用者写出简短的代码，
同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。
```
- property的内部结构

###代码解析
```
@property本身又创建了另一个装饰器@score.setter，
负责把一个setter方法变成属性赋值，于是，我们就拥
有一个可控的属性操作
```
```
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
```

<!-- ctr+Q了解文档相关信息 ，了解property的内部信息-->
```
s=Student()
print(s.set_score(89))
print(s.get_score())

k=property()
k=property(1,14,)
print(k.fget)
print(k.fset)

# None
# 89
# 1
# 14
```
