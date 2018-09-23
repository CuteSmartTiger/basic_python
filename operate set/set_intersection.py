# 求交集

ses = {'s', 'a', 'j', 'd', 'f'}
di = {1,2,3,'s','j'}
st = 'msnakfj'
f = frozenset({'s','j','a',2})
# 方法一：intersection(Iterable)
# res的类型是由ses决定的
res = ses.intersection(di)
print(res,ses,type(res))
# {'s', 'j'} {'s', 'j', 'f', 'd', 'a'} <class 'set'>

res = f.intersection(di)
print(res,f,type(res))
# frozenset({'s', 2, 'j'}) frozenset({'s', 'a', 2, 'j'}) <class 'frozenset'>

res = ses.intersection(st)
print(res,ses,type(res))
# {'j', 'f', 's', 'a'} {'j', 'a', 's', 'd', 'f'} <class 'set'>


print('----------fangfa2-------')
# 方法二：&
ses = {'s', 'a', 'j', 'd', 'f'}
di = {1,2,3,'s','j'}
st = 'msnakfj'
f = frozenset({'s','j','a',2})
res = ses&di
print(res,ses,type(res))
# {'j', 's'} {'d', 'f', 'j', 's', 'a'} <class 'set'>



print('------intersection_update 会将原集合改变,只可以用于可变集合--------')
ses = {'s', 'a', 'j', 'd', 'f'}
di = {1,2,3,'s','j'}
st = 'msnakfj'
f = frozenset({'s','j','a',2})
res = ses.intersection_update(di)
print(res,ses,type(res))
# None {'s', 'j'} <class 'NoneType'>