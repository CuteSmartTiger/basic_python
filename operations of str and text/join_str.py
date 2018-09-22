# 了解一个方法从四个方面下手：
# 作用：
# 语法：
# 参数：
# 返回值，返回类型


# 方法一：+

# 方法二：format 或者 %s


# 方法三：''.join()


print('KKK'   'LLLLL\a')
kj = 'kkkjkkkk'
# 非贪心算法
print(kj.find('jk'))
h = 'nnnnniiiii hao liu lao hu  '
print(h.lstrip('ni'))

# 字符串的分割：
# 按指定字符分割成三个元素的元组
# \n  换行
# \r  回车
hu = 'liuhu\n liuli\r yaoyao\n'
new_hu = hu.partition('\n')
print(new_hu)

# 按行分割
t_hu = hu.splitlines(True)   #['liuhu\n', ' liuli\r', ' yaoyao\n']
print(t_hu)

# 判断
h='oo3'
print(h.isalpha())   #False
print(h.isalnum())   #True