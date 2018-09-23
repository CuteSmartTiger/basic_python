def test():
    print('start')
    res = yield 1
    print(res)

    res1 = yield 2
    print(res1)

    res2 = yield 3
    print(res2)


g = test()
print(g.send(None))
print(g.send('hh'))
g.close()
print(g.send('bb'))