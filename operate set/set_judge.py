ses = {'s', 'a', 'j', 'd', 'f'}
di = {1,2,3,'s','j'}
d = {'m'}
# 针对不存在交集进行判断
res = ses.isdisjoint(di)
res1 = ses.isdisjoint(d)
print(res)
# False
print(res1)
#True

print('-------issuper-')
ses = {'s', 'a', 'j', 'd', 'f'}
di = {'s','j'}
d = {'m'}
# 针对不存在交集进行判断
res = ses.issuperset(di)
res1 = ses.issuperset(d)
print(res)
# True
print(res1)
#False


print('-------issubset------')
ses = {'s', 'a', 'j', 'd', 'f'}
di = {'s','j'}
d = {'m'}
# 针对不存在交集进行判断
res = ses.issubset(di)
res1 = di.issubset(ses)
print(res)
# False
print(res1)
#True

