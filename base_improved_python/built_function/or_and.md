##or 与 and的用法
or是从左到右计算表达式，返回第一个为真的
and ：从左到右计算表达式，若所有值均为真，则返回最后一个值，若存在假，返回第一个假值




####示例
```
bool(list) = True
bool(tuple) = True
list 和 tuple 都有布尔值的
所以list or tuple = list
list and tuple = tuple
tuple or list = tuple
tuple and list = list
和isinstance()无关
```
