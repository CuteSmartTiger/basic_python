# 打乱
import random
nums = [1,2,2,3,2,4,2,6]
res = random.shuffle(nums)
print(res)   #None
print(nums)  #[1, 4, 2, 6, 2, 2, 3, 2]

# print(random())   之间的区别

print('''------------反转----------''')
# 反转
nums = [1,2,2,3,2,4,2,6]
res = nums.reverse()
print(res)    #None
print(nums)   #[6, 2, 4, 2, 3, 2, 2, 1]

nums = [1,2,2,3,2,4,2,6]
res = nums[::-1]
print(res)    #[6, 2, 4, 2, 3, 2, 2, 1]
print(nums)   #[1, 2, 2, 3, 2, 4, 2, 6]