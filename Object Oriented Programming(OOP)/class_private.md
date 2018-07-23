##下划线

###前方双下划线
- 让内部属性不被外部访问，私有变量
```
可以把属性的名称前加上两个下划线__
```

- 代码示例解析
```
class Person(object):
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        if gender == 'female' or gender == 'male':
            self.__gender=gender
            return self.__gender
        else:
            raise ValueError('性别错误')


c=Person('liuhu','mel')
print(c.get_gender())
print(c.set_gender('male'))
print(c.get_gender())

# mel
# male
# male

后续可以用装饰优化
```

###__init__ 前后双下划线  
- 特殊变量




###单下划线
