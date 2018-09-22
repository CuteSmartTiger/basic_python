# 定义
# 列表生成器
num = range(1,10,2)             #range(1, 10, 2)
nums = list(range(1,10,2))         #1, 3, 5, 7, 9]
print(nums)
print(num)
print(num[0])   #1

print('--------------append---------------')
# 为列表增加新的元素对象，元素可以时字符串 列表 字典 等等
# 增加的几种方法：
num = [1,2,3]
# 添加：
print(num.append(6))  #None
print(num)

print('--------------extend---------------')
# 扩充一个可迭代对象，对象时一个可迭代对象，将对象迭代后添加到列表中
nums2=['a','b']
str1= 'asdfs'
print(nums2.extend(str1))   #返回值为None
print(nums2)

print('--------------+号---------------')
# 扩充一个可迭代对象，对象时一个可迭代对象，将对象迭代后添加到列表中
# 此方法类型必须一样
nums2=['a','b']
str1= [1]
print(nums2+str1)



print('------------删除操作---------------')
print('------------del---------------')
lis = [1,2,3,2,2,2,6]
del lis[1]    #删除指定索引位置的元素
print(lis)

print('------------pop---------------')
lis = [1,2,3,2,4,2,6]
res = lis.pop(-3)    #删除指定索引位置的元素,默认为-1，并返回删除的元素对象
print(res)           #4
print(lis)           #lis = [1,2,3,2,4,2,6]


print('-------------remove--------------')
lis = [1,2,2,3,2,4,2,6]
res = lis.remove(2)    #删除指定对象，若对象重复有多个，则删除最左边的,返回None，若不存在就报错
print(res)           #None
print(lis)           #lis = [1, 3, 2, 4, 2, 6]

# remove循环遍历删除的坑
lis = [1,2,2,3,2,4,2,6]
for num in lis:
    if num == 2:
        lis.remove(num)
print(lis)   #[1, 3, 4, 2, 6]

# 改：
lis[2] = 5  #[1, 3, 5, 2, 6]
print(lis)


print('-------------获取--------------')
lis = [1,2,2,3,2,4,2,6]
# 根据索引获取
print(lis[4])   #2

# 获取元素对象的索引
print(lis.index(2))   #1  若不存在此元素，则报错

# 获取元素的数量
print(lis.count(2))   #4

# 切片
print(lis[1:6:2])     #[2, 3, 4]


