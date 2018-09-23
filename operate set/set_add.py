# 添加
# 方法1：add() 传入的参数必须是不可变的，需要可哈希，传入列表就报错
se = {'s', 'k', 'a', 'j', 'd', 'f'}
res = se.add(3)   #None
print(res,se,type(se))

# 方法2：update(Iterable)  将参数转换为集合，然后再进行运算，参数类型
# 可以是字典  元组 集合 列表，这些数据类型中的元素必须是可哈希的，即不
# 可变的元素，若列表中嵌套列表，则会报错
se = {'s', 'k', 'a', 'j', 'd', 'f'}
s = {1,2,'adc'}
s1 = (1,10)

s3 = {'name':'liuhu','age':12}
# 更新添加集合
res = se.update(s)      #None
se = {'s', 'k', 'a', 'j', 'd', 'f'}
print(res,se,type(se))
# {'a', 'k', 'j', 'f', 's', 'd'} <class 'set'>

# 添加元组
res = se.update(s1)      #None
print(res,se,type(se))
# {1, 'a', 10, 'k', 'j', 'f', 's', 'd'} <class 'set'>

# 添加列表
# 若列表中嵌套列表，则会报错,即当s2 = [1,2,[3]]时会报错
s2 = [3,4]
se = {'s', 'k', 'a', 'j', 'd', 'f'}
res = se.update(s2)      #None
print(res,se,type(se))
# {3, 4, 'k', 's', 'f', 'a', 'd', 'j'} <class 'set'>


se = {'s', 'k', 'a', 'j', 'd', 'f'}
res = se.update(s3)      #None
print(res,se,type(se))
# {'name', 'k', 's', 'f', 'a', 'age', 'd', 'j'} <class 'set'>

# 将传入的字符串拆开然后添加到集合
se = {'s', 'k', 'a', 'j', 'd', 'f'}
res = se.update('op')      #None
print(res,se,type(se))
# None {'j', 'a', 'o', 'p', 's', 'd', 'f', 'k'} <class 'set'>


# 针对可变集合：
# 无