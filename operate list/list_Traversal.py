nums = [1,2,2,3,2,4,2,6]
# 1.遍历元素
for num in nums[::-1]:
    # 这个方法无法同时获取元素的正确索引
    print(num,nums.index(num))

# 2.通过索引遍历
total_nums = len(nums)
for i in range(total_nums):
    print(i,nums[i])

# 3.通过枚举获取
print(list(enumerate(nums, 1)))  #[(1, 1), (2, 2), (3, 2), (4, 3), (5, 2), (6, 4), (7, 2), (8, 6)]
for dix,value in enumerate(nums,1):
    print(dix,value)

for num in enumerate(nums,1):
    print(num)

# 迭代器遍历
nums = [1,2,2,3,2,4,2,6]
# 创建一个迭代器对象
iter_nums = iter(nums)

# 迭代器也是可迭代对象，可以for in 遍历
for nu in iter_nums:
    print(nu)

# 第二遍遍历失效，迭代器只可以遍历一次
for nu in iter_nums:
    print(nu)

print('----next-----')
# 迭代器的next方法
nums = [1,2,2,3,2,4,2,6]
# 创建一个迭代器对象,迭代器可以记录索引位置
iter_nums = iter(nums)
print(next(iter_nums))
print(next(iter_nums))
print(next(iter_nums))

