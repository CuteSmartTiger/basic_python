# 并集
ses = {'s', 'a', 'j', 'd', 'f'}
di = {1,2,3,'s','j'}
st = 'msnakfj'
f = frozenset({'s','j','a',2})

# 方法一：union()
res = ses.union(di)
print(res,ses,type(res))
# {1, 'a', 'd', 2, 3, 'j', 's', 'f'} {'a', 'd', 'j', 's', 'f'} <class 'set'>


# 方法2：|
res = ses|di
print(res,ses,type(res))
# {1, 'f', 2, 3, 'd', 's', 'a', 'j'} {'f', 'd', 's', 'a', 'j'} <class 'set'>

print('----------update 方法将改变调用对象')
# 方法3：update()
ses = {'s', 'a', 'j', 'd', 'f'}
di = {1,2,3,'s','j'}
st = 'msnakfj'
f = frozenset({'s','j','a',2})

res = ses.update(di)
print(res,ses,type(res))
# None {1, 2, 3, 'd', 'j', 's', 'f', 'a'} <class 'NoneType'>