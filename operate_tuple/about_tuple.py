# 不可变对象
h = (1,)
print('h',type(h))   #h <class 'tuple'>
g = (1)
print('g',type(g))   #g <class 'int'>

tu = (1,2,4,6,23,78)
# 获取
print(tu[::-1])  #(78, 23, 6, 4, 2, 1)
print(tu[1:6:2])  #(2, 6, 78)

tu = (1,2,4,6,2,3,423,78)
print(tu.count(2))   #2
print(tu.count(14))  #0
print(tu.index(6))   #3

# 拼接
print((1,2)*3)   #1, 2, 1, 2, 1, 2)
print((1,2)+(1,2))   #（1, 2, 1, 2)

# 拆包
a, b = ('a',3)
print(a, b)   #a 3

a, b = 'a',3
print(a, b)   #a 3

# 额外知识点：交换
a=1
b=2
a,b=b,a
print(a,b)