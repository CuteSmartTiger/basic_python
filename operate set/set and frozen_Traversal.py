ses = {'s', 'k', 'a', 'j', 'd', 'f'}
for se in ses:
    print(se)

s = iter(ses)

for i in s:
    print(i)

s = iter(ses)
next(s)

print('---------frozenset()-------')
ses = frozenset({'s', 'k', 'a', 'j', 'd', 'f'})
for se in ses:
    print(se)

s = iter(ses)

for i in s:
    print(i)

s = iter(ses)
next(s)