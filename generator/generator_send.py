# send有一个参数，指定的是上一次被挂起的yield语句的返回值
# 第一次调用send()方法时，需要传值None
def test():
    print('start')
    res = yield 1
    print(res)

    res1 = yield 2
    print(res1)

g = test()
print(g.send(None))
print(g.send('hh'))
# start
# 1
# hh
# 2