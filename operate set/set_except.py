# 差集
ses = {'s', 'a', 'j', 'd', 'f'}
di = {1,2,3,'s','j'}
st = 'msnakfj'
f = frozenset({'s','j','a',2})

# 方法一：difference()
res = ses.difference(di)
print(res,ses,type(res))
# {'d', 'f', 'a'} {'f', 'j', 'a', 'd', 's'} <class 'set'>


# 方法2：减号 '-'
res = ses-di
print(res,ses,type(res))
# {'f', 'd', 'a'} {'d', 'j', 's', 'a', 'f'} <class 'set'>

print('----------update 方法将改变调用对象')
# 方法3：difference_update()
ses = {'s', 'a', 'j', 'd', 'f'}
di = {1,2,3,'s','j'}
st = 'msnakfj'
f = frozenset({'s','j','a',2})

res = ses.difference_update(di)
print(res,ses,type(res))
# None {'a', 'd', 'f'} <class 'NoneType'>