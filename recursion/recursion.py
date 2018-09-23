# 注意两点：
# 传递
# 回归
def jiecheng(n):
    if n==1:
        return 1
    return n*jiecheng(n-1)

print(jiecheng(4))
