# 方法1：生成器推导式
# 原始方法：
L = [ i for i in range(10000) if i % 9 ==0]
print(L)
generator_L = iter(L)
print(next(generator_L))

# 此方法优化：将中括号改为圆扩号
gene = ( i for i in range(10000) if i % 9 ==0)

print(next(gene))
print(gene.__next__())

# 方法二：生成器函数  使用yield
def tes():
    for i in range(1,200):
        yield i

print(next(tes()))