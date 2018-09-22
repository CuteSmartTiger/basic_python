# 方法一：sorted()
# 内建函数，排序对象为可迭代对象，功能强大，可以按指定
# 的关键字进行排序，也可以倒序排序,返回排序后的列表，原列表不变化
nums = [(1,'a'),(4,'c'),(2,'f'),(8,'e')]
result = sorted(nums)
print(result)   #[(1, 'a'), (2, 'f'), (4, 'c'), (8, 'e')]
print(nums)           #[(1, 'a'), (4, 'c'), (2, 'f'), (8, 'e')]

print('----------按关键字排序--------')
# 获取关键字
def getkey(x):
    return x[1]

nums = [(1,'a'),(4,'c'),(2,'f'),(8,'e')]
result = sorted(nums,key=getkey)
print(result)  #[(1, 'a'), (4, 'c'), (8, 'e'), (2, 'f')]

nums = [(1,'a'),(4,'c'),(2,'f'),(8,'e')]
result = sorted(nums,key = lambda x:x[1])
print(result)  #[(1, 'a'), (4, 'c'), (8, 'e'), (2, 'f')]

nums = [(1,'a'),(4,'c'),(2,'f'),(8,'e')]
result = sorted(nums,key = lambda x:x[1],reverse=True)
print(result)   #[(2, 'f'), (8, 'e'), (4, 'c'), (1, 'a')]


# 方法二：sort  列表对象方法，只针对列表
nums = [(1,'a'),(4,'c'),(2,'f'),(8,'e')]
result = nums.sort(key = lambda x:x[1],reverse=True)
print(result)   #None
print(nums)#[(2, 'f'), (8, 'e'), (4, 'c'), (1, 'a')]