# 方法1：remove 删除集合中指定的元素，若不存在则报错
se = {'s', 'k', 'a', 'j', 'd', 'f'}
res = se.remove('k')
print(se,res)
# {'d', 'f', 's', 'j', 'a'} None


# 方法2：discard 删除集合中指定的元素，若不存在则返回None
se = {'s', 'k', 'a', 'j', 'd', 'f'}
res = se.discard('g')
print(se,res)
# {'a', 'j', 'd', 'f', 'k', 's'} None

# 方法三：因为集合是无序的，所以pop为随机删除，若集合为空，则报错
se = {'s', 'k', 'a', 'j', 'd', 'f'}
res = se.pop()
print(se,res)
# {'f', 's', 'd', 'k', 'j'} a


# 方法四：clear  清空集合，集合变量还存在
se = {'s', 'k', 'a', 'j', 'd', 'f'}
res = se.clear()
print(se,res)
# set() None

# 方法5：del 删除集合，集合不存在
se = {'s', 'k', 'a', 'j', 'd', 'f'}
del se
# print(se)   #报错
