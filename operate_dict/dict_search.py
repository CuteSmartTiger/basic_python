# 方法1
person = {'name':'liuhu','age':18}
dic = {'e': 7,'a': 1, 'd': 4,  's': 5}
print(person['name'])

# 方法2
res = person.get('name','mei')
print(res)
res = person.get('nam','mei')
print(res)

# 方法三：
res = person.setdefault('na1','def')
print(res)
print(person)