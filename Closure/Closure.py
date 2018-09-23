# 概念：
# 在函数嵌套的前提下
# 内层函数引用外层函数的变量或者参数
# 外层函数又把内层函数当返回值返回
# 这个内层函数加所引用的外层变量，称为闭包

def test():
    a=20
    def go():
        print(a)
    return go
viewfucn = test()
viewfucn()


# 应用场景
# 使用闭包会比较简洁好看，多个地方使用时可以直接调用viewfucn()


print('------------当期函数示例---------')
# 示例：
def test1():
    res = []
    for i in range(1,5):
        def test2():
            print(i)
        res.append(test2)
    return res

tes = test1()
print(tes)
print(tes[0]())
print(tes[1]())
print(tes[2]())
print(tes[3]())

print('--------------使用闭包进行改进-------------')
# 改进：通过闭包记录变量的值进行改进
def test1():
    res = []
    for i in range(1,5):
        def test2(i):
            num = i
            def inner():
                print(num)
            return inner
        res.append(test2(i))
    return res

tes = test1()
print(tes)
print(tes[0]())
print(tes[1]())
print(tes[2]())
print(tes[3]())