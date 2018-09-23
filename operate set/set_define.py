# 可变集合：<class 'set'>
# 方法1
s1 = {1,2,3,4}

# 方法2：set(iterable)
s2 = set('adsakjf')
print(s2,type(s2))                                 #{'d', 'k', 'f', 'j', 'a', 's'}
s3 = set([1,2,3,4])
print(s3)                                #{1, 2, 3, 4}
s4 = set({'name':'liuhu','age':18})
print(s4)                                 #{'age', 'name'}
s5 = set((1,2,3,5))
print(s5)                                 #{1, 2, 3, 5}

# 方法三： 集合推导式
ss = set(i for i in range(10) if i%2 ==0)
print(ss)  #{0, 2, 4, 6, 8}
sss = {i for i in range(10) if i%2 ==0}
print(sss)  #{0, 2, 4, 6, 8}


print('----------------frozenset---------')
# 不可变集合:
# 方法1：frozenset(iterable)

s2 = frozenset('adsakjf')
print(s2,type(s2))
s3 = frozenset([1,2,3,4])
print(s3)
s4 = frozenset({'name':'liuhu','age':18})
print(s4)
s5 = frozenset((1,2,3,5))
print(s5)

# frozenset({'s', 'k', 'a', 'j', 'd', 'f'}) <class 'frozenset'>
# frozenset({1, 2, 3, 4})
# frozenset({'age', 'name'})
# frozenset({1, 2, 3, 5})

# 方法2： 集合推导式
ss = frozenset(i for i in range(10) if i%2 ==0)
print(ss)  #{frozenset({0, 2, 4, 6, 8})

# 注意：
# 空集合的定义方式为：
# s=set()
# s=frozenset()
# 集合中的元素必须可哈希，即不可变对象，不可以是列表或者字典
print({1,2,(1,2)})